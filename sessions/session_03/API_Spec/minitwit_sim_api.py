# -*- coding: utf-8 -*-

"""
    ITU-MiniTwit Simulator API
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    An API for the simulator for ITU-MiniTwit, a microblogging application
    written with Flask and sqlite3.

    :copyright: (c) 2019 by HelgeCPH.
    :license: BSD, see LICENSE for more details.
"""
import os
import time
import sqlite3
from hashlib import md5
from pathlib import Path
from datetime import datetime
from contextlib import closing
from flask import Flask, request, g, jsonify, abort
from werkzeug.security import check_password_hash, generate_password_hash
from minitwit import connect_db, query_db, DATABASE, SECRET_KEY, init_db

# Delete database for testing
Path(DATABASE).unlink(missing_ok=True)
Path("latest_processed_sim_action_id.txt").unlink(missing_ok=True)
init_db()

# configuration
DEBUG = True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def not_req_from_simulator(request):
    from_simulator = request.headers.get("Authorization")
    if from_simulator != "Basic c2ltdWxhdG9yOnN1cGVyX3NhZmUh":
        error = "You are not authorized to use this resource!"
        return jsonify({"status": 403, "error_msg": error}), 403


def get_user_id(username):
    user_id = query_db(
        "SELECT user.user_id FROM user WHERE username = ?", [username], one=True
    )
    if user_id:
        return user_id["user_id"]
    else:
        return None


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()


@app.after_request
def after_request(response):
    """Closes the database again at the end of the request."""
    g.db.close()
    return response


def update_latest(request: request):
    parsed_command_id = request.args.get("latest", type=int, default=-1)
    if parsed_command_id != -1:
        with open("./latest_processed_sim_action_id.txt", "w") as fp:
            fp.write(str(parsed_command_id))


# get the latest value
@app.route("/latest", methods=["GET"])
def get_latest():
    with open("./latest_processed_sim_action_id.txt") as fp:
        content = fp.read()

    try:
        latest_processed_command_id = int(content)
    except:
        latest_processed_command_id = -1
    return jsonify({"latest": latest_processed_command_id})


@app.route("/register", methods=["POST"])
def register():
    update_latest(request)

    request_data = request.json

    error = None
    if request.method == "POST":
        if not request_data["username"]:
            error = "You have to enter a username"
        elif not request_data["email"] or "@" not in request_data["email"]:
            error = "You have to enter a valid email address"
        elif not request_data["pwd"]:
            error = "You have to enter a password"
        elif get_user_id(request_data["username"]) is not None:
            error = "The username is already taken"
        else:
            query = """INSERT INTO user
                       (username, email, pw_hash) VALUES (?, ?, ?)"""
            g.db.execute(
                query,
                [
                    request_data["username"],
                    request_data["email"],
                    generate_password_hash(request_data["pwd"]),
                ],
            )
            g.db.commit()

    if error:
        return jsonify({"status": 400, "error_msg": error}), 400
    else:
        return "", 204


@app.route("/msgs", methods=["GET"])
def messages():
    update_latest(request)

    not_from_sim_response = not_req_from_simulator(request)
    if not_from_sim_response:
        return not_from_sim_response

    no_msgs = request.args.get("no", type=int, default=100)
    if request.method == "GET":
        query = """SELECT message.*, user.* FROM message, user
        WHERE message.flagged = 0 AND message.author_id = user.user_id
        ORDER BY message.pub_date DESC LIMIT ?"""

        messages = query_db(query, [no_msgs])

        filtered_msgs = []
        for msg in messages:
            filtered_msg = {}
            filtered_msg["content"] = msg["text"]
            filtered_msg["pub_date"] = msg["pub_date"]
            filtered_msg["user"] = msg["username"]
            filtered_msgs.append(filtered_msg)

        return jsonify(filtered_msgs)


@app.route("/msgs/<username>", methods=["GET", "POST"])
def messages_per_user(username):
    update_latest(request)

    not_from_sim_response = not_req_from_simulator(request)
    if not_from_sim_response:
        return not_from_sim_response

    no_msgs = request.args.get("no", type=int, default=100)
    if request.method == "GET":

        user_id = get_user_id(username)
        if not user_id:
            abort(404)

        query = """SELECT message.*, user.* FROM message, user
                   WHERE message.flagged = 0 AND
                   user.user_id = message.author_id AND user.user_id = ?
                   ORDER BY message.pub_date DESC LIMIT ?"""
        messages = query_db(query, [user_id, no_msgs])

        filtered_msgs = []
        for msg in messages:
            filtered_msg = {}  # return '', 204}
            filtered_msg["content"] = msg["text"]
            filtered_msg["pub_date"] = msg["pub_date"]
            filtered_msg["user"] = msg["username"]
            filtered_msgs.append(filtered_msg)

        return jsonify(filtered_msgs)

    # post message as <username>
    elif request.method == "POST":
        request_data = request.json
        query = """INSERT INTO message (author_id, text, pub_date, flagged)
                   VALUES (?, ?, ?, 0)"""
        g.db.execute(
            query,
            (get_user_id(username), request_data["content"], int(time.time())),
        )
        g.db.commit()
        return "", 204


@app.route("/fllws/<username>", methods=["GET", "POST"])
def follow(username):
    update_latest(request)

    not_from_sim_response = not_req_from_simulator(request)
    if not_from_sim_response:
        return not_from_sim_response

    user_id = get_user_id(username)

    if not user_id:
        abort(404)

    no_followers = request.args.get("no", type=int, default=100)

    if request.method == "POST" and "follow" in request.json.keys():
        follows_username = request.json["follow"]
        follows_user_id = get_user_id(follows_username)
        if not follows_user_id:
            # TODO: This has to be another error, likely 500???
            abort(404)

        query = """INSERT INTO follower (who_id, whom_id) VALUES (?, ?)"""
        g.db.execute(query, [user_id, follows_user_id])
        g.db.commit()

        return "", 204

    elif request.method == "POST" and "unfollow" in request.json.keys():
        unfollows_username = request.json["unfollow"]
        unfollows_user_id = get_user_id(unfollows_username)
        if not unfollows_user_id:
            # TODO: This has to be another error, likely 500???
            abort(404)

        query = "DELETE FROM follower WHERE who_id=? and WHOM_ID=?"
        g.db.execute(query, [user_id, unfollows_user_id])
        g.db.commit()

        return "", 204

    elif request.method == "GET":
        no_followers = request.args.get("no", type=int, default=100)
        query = """SELECT user.username FROM user
                   INNER JOIN follower ON follower.whom_id=user.user_id
                   WHERE follower.who_id=?
                   LIMIT ?"""
        followers = query_db(query, [user_id, no_followers])
        follower_names = [f["username"] for f in followers]
        followers_response = {"follows": follower_names}

        return jsonify(followers_response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

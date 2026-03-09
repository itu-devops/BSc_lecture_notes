"""
Call me for example like:

$ python minitwit_simulator.py "http://localhost:5001"
"""

import traceback
import os
import csv
import sys
import json
import http
import socket
import base64
import requests
from time import sleep
from datetime import datetime
from contextlib import closing
import sqlite3


CSV_FILENAME = "./minitwit_scenario.csv"
USERNAME = "simulator"
PWD = "super_safe!"
CREDENTIALS = ":".join([USERNAME, PWD]).encode("ascii")
ENCODED_CREDENTIALS = base64.b64encode(CREDENTIALS).decode()
HEADERS = {
    "Connection": "close",
    "Content-Type": "application/json",
    f"Authorization": f"Basic {ENCODED_CREDENTIALS}",
}


def get_actions():

    # read scenario .csv and parse to a list of lists
    with open(CSV_FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t", quotechar=None)

        # for each line in .csv
        for line in reader:
            try:
                # we know that the command string is always the fourth element
                command = line[3]

                command_id = int(line[0])
                delay = int(line[1])
                user = line[4]
                if command == "register":
                    email = line[5]
                    user_pwd = line[-1]

                    item = {
                        "latest": command_id,
                        "post_type": command,
                        "username": user,
                        "email": email,
                        "pwd": user_pwd,
                    }

                    yield item, delay

                elif command == "tweet":
                    tweet_content = line[5]
                    item = {
                        "latest": command_id,
                        "post_type": command,
                        "username": user,
                        "content": tweet_content,
                    }

                    yield item, delay

                elif command == "follow":
                    user_to_follow = line[5]
                    item = {
                        "latest": command_id,
                        "post_type": command,
                        "username": user,
                        "follow": user_to_follow,
                    }
                    yield item, delay

                elif command == "unfollow":
                    user_to_unfollow = line[5]

                    item = {
                        "latest": command_id,
                        "post_type": command,
                        "username": user,
                        "unfollow": user_to_unfollow,
                    }
                    yield item, delay

                else:
                    # This should never happen and can likely be removed to
                    # make parsing for plot generation later easier
                    print("Unknown type found: (" + command + ")")

            except Exception as e:
                print("========================================")
                print(traceback.format_exc())


def main(host):
    for action, delay in get_actions():
        try:
            # SWITCH ON TYPE
            command = action["post_type"]
            reponse = None

            if command == "register":

                # build url for request
                url = f"{host}/register"

                # Set parameters: latest
                params = {"latest": action["latest"]}
                # Set data: username, email, pwd
                data = {
                    "username": action["username"],
                    "email": action["email"],
                    "pwd": action["pwd"],
                }

                response = requests.post(
                    url,
                    data=json.dumps(data),
                    params=params,
                    headers=HEADERS,
                    timeout=0.3,
                )

                # error handling (204 success, 400 user exists)
                # 400 user exists already but not an error to log
                if not (
                    (response.status_code == 204)
                    or (response.status_code == 400)
                ):
                    ts_str = datetime.strftime(
                        datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                    )
                    print(
                        ",".join(
                            [
                                ts_str,
                                host,
                                str(action["latest"]),
                                str(response.status_code),
                                command,
                            ]
                        )
                    )

                response.close()

            elif command == "msgs":

                # LIST method. Not used atm.
                # build url for request
                url = f"{host}/msgs"

                # Set parameters: latest & no (amount)
                params = {"latest": action["latest"], "no": action["no"]}

                response = requests.post(
                    url, params=params, headers=HEADERS, timeout=0.3
                )

                # error handling (200 success, 403 failure (no headers))

                # 403 bad request
                if response.status_code != 200:
                    ts_str = datetime.strftime(
                        datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                    )
                    print(
                        ",".join(
                            [
                                ts_str,
                                host,
                                str(action["latest"]),
                                str(response.status_code),
                                command,
                            ]
                        )
                    )

                response.close()

            elif command == "follow":

                # build url for request
                username = action["username"]
                url = f"{host}/fllws/{username}"

                # Set parameters: latest
                params = {"latest": action["latest"]}
                # Set data: content
                data = {"follow": action["follow"]}  # value for user to follow

                response = requests.post(
                    url,
                    data=json.dumps(data),
                    params=params,
                    headers=HEADERS,
                    timeout=0.3,
                )

                # error handling (204 success, 403 failure, 404 Not Found no user id)

                # 403 unauthorized or 404 Not Found
                if response.status_code != 204:
                    ts_str = datetime.strftime(
                        datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                    )
                    print(
                        ",".join(
                            [
                                ts_str,
                                host,
                                str(action["latest"]),
                                str(response.status_code),
                                command,
                            ]
                        )
                    )

                response.close()

            elif command == "unfollow":

                # build url for request
                username = action["username"]
                url = f"{host}/fllws/{username}"
                # Set parameters: latest
                params = {"latest": action["latest"]}
                # Set data: content
                # value for user to follow
                data = {"unfollow": action["unfollow"]}

                response = requests.post(
                    url,
                    data=json.dumps(data),
                    params=params,
                    headers=HEADERS,
                    timeout=0.3,
                )

                # error handling (204 success, 403 failure, 404 Not Found no user id)

                # 403 unauthorized or 404 Not Found
                if response.status_code != 204:
                    ts_str = datetime.strftime(
                        datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                    )
                    print(
                        ",".join(
                            [
                                ts_str,
                                host,
                                str(action["latest"]),
                                str(response.status_code),
                                command,
                            ]
                        )
                    )

                response.close()

            elif command == "tweet":

                # build url for request
                username = action["username"]
                url = f"{host}/msgs/{username}"
                # Set parameters: latest
                params = {"latest": action["latest"]}
                # Set data: content
                data = {"content": action["content"]}

                response = requests.post(
                    url,
                    data=json.dumps(data),
                    params=params,
                    headers=HEADERS,
                    timeout=0.3,
                )

                # error handling (204 success, 403 failure)
                # 403 unauthorized
                if response.status_code != 204:
                    ts_str = datetime.strftime(
                        datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                    )
                    print(
                        ",".join(
                            [
                                ts_str,
                                host,
                                str(action["latest"]),
                                str(response.status_code),
                                command,
                            ]
                        )
                    )

                response.close()

            else:
                # throw exception. Should not be hit
                ts_str = datetime.strftime(
                    datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                )
                print(
                    ",".join(
                        [
                            "FATAL: Unknown message type",
                            ts_str,
                            host,
                            str(action["latest"]),
                        ]
                    )
                )

        except requests.exceptions.ConnectionError as e:
            ts_str = datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
            print(
                ",".join(
                    [ts_str, host, str(action["latest"]), "ConnectionError"]
                )
            )
        except requests.exceptions.ReadTimeout as e:
            ts_str = datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
            print(
                ",".join([ts_str, host, str(action["latest"]), "ReadTimeout"])
            )
        except Exception as e:
            print("========================================")
            print(traceback.format_exc())
            ts_str = datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
            print(
                ",".join(
                    [ts_str, host, str(action["latest"]), type(e).__name__]
                )
            )

        sleep(delay / (1000 * 100000))


if __name__ == "__main__":
    host = sys.argv[1]

    main(host)

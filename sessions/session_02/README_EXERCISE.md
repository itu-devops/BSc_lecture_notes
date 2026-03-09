# Exercises

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>


## Getting accustomed using Docker and Docker Compose

  - Navigate to https://github.com/itu-devops/flask-minitwit-mongodb/tree/Containerize (**branch `Containerize`**) and work through the scenario given in the [`README.md`](https://github.com/itu-devops/flask-minitwit-mongodb/tree/Containerize) file.

```bash
$ git clone https://github.com/itu-devops/flask-minitwit-mongodb.git
$ cd flask-minitwit-mongodb
$ git checkout Containerize
```
  - Make sure with your group fellows, that you understand what you are doing in every step. If in doubt, explain to each other what you think is going on.

Once done reproducing the given scenario, modify the `docker-compose.yml` file to include another container `clidownload`, which is an instance of the image `appropriate/curl`. It should download all tweets from the web-application as HTML text. If in doubt, consult the lecture notes for inspiration.


## Create a dependency graph of your application

Create an "as-complete-as-possible" dependency graph for your refactored version of _ITU-MiniTwit_ (task from last week for Sunday).

You might want to use [`debtree`](https://manpages.ubuntu.com/manpages/jammy/man1/debtree.1.html) to create a dependency graph of the Debian packages that your application uses and [`pipdeptree`](https://pypi.org/project/pipdeptree/) for the pure Python dependencies.

For each edge (arrow) that indicates a direct dependency from your application identify if it is a runtime dependency or if it is a build-/compile-time dependency.

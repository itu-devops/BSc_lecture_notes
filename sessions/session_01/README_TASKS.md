# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>


  - [1) Adding Version Control](#1-adding-version-control)
  - [2) Try to develop a high-level understanding of _ITU-MiniTwit_.](#2-try-to-develop-a-high-level-understanding-of-itu-minitwit)
  - [3) Migrate _ITU-MiniTwit_ to run on a modern computer running Linux](#3-migrate-itu-minitwit-to-run-on-a-modern-computer-running-linux)
  - [4) Share your Work on GitHub](#4-share-your-work-on-github)
  - [5) Preparation for next time](#5-preparation-for-next-time)


## 1) Adding Version Control


Before starting your refactoring work, convert the contents of the directory `itu-minitwit` into a Git repository and add all files to it so that you can always go back to the beginning of your work, i.e., the very first commit in your repositories should contain the code _as taken over_ without any modification yet.

In case you are in doubt about converting a directory of files into a Git repository, check chapter 2 _"Git Basics"_ from the free online [Pro Git book](https://git-scm.com/book/en/v2) also the [preparation material](../session_02/README_PREP.md) for next week might serve as a starting point.


## 2) Try to develop a high-level understanding of _ITU-MiniTwit_.

Throughout the semester you will work on your own version of _ITU-MiniTwit_, which will be in many ways similar to the version you just took over. Therefore, it is worth to understand how it is working. Perhaps it is best to start your investigation on the top of the file `minitwit.py`, followed by the function `timeline()`, the functions `before_request()` and `after_request()`, and then all the other functions.

As described in class, _ITU-MiniTwit_ relies on the web-application framework [Flask](https://palletsprojects.com/p/flask/). The [official documentation](https://flask.palletsprojects.com/en/) as well as the book [Flask Web Development](https://www.oreilly.com/library/view/flask-web-development/9781491991725/) might support you in this task. In case you are in doubt about some Python constructs, the free book [Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/) might be helpful.


#### Why do we do that? Why do I have to understand other peoples' code?

  > Unfortunately, computer programming education often focuses on how to single-handedly develop programs from scratch in a single language and single execution environment, a development style prevalent in the 1950s and 60s. Nowadays, software development is typically a team-based activity and most often involves extending and maintaining existing systems written in a multitude of languages for diverse execution environments. It’s now even more important to understand code concepts, forms, structures, and idioms to be able to write code that other programmers can read easily.
  >
  > [Diomidis Spinellis _"Reading, Writing, and Code: The key to writing readable code is developing good coding style."_](https://dl.acm.org/doi/pdf/10.1145/957717.957782)

Many of the barriers for taking over an existing system are also identified as issues when joining an open-source community in [Steinmacher et al. _"Let Me In: Guidelines for the Successful Onboarding of Newcomers to Open Source Projects"_](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8254320&tag=1)


## 3) Migrate _ITU-MiniTwit_ to run on a modern computer running Linux

By "modern computer", we mean your personal computer running, e.g., Linux.

### What do you need?

  * A modern Python, i.e., version >= 3.12,
    - There are various ways of installing it, either via the system's package manager (`apt search python3`)
    - manually from [python.org](https://www.python.org/downloads/)
    - via [pyenv](https://github.com/pyenv/pyenv)
    - via [Anaconda](https://www.anaconda.com/products/individual)
  * The Python dependencies from `itu-minitwit`:
    - [Flask](https://flask.palletsprojects.com/en/3.0.x/) >= version 3.0.0
      - [Werkzeug](https://palletsprojects.com/p/werkzeug/) >= version 3.0.0
      - [Jinja2](https://palletsprojects.com/p/jinja/) >= version 3.0.0
  * A current C compiler, e.g., `gcc`
    - Likely it is already part of your Linux installation.
    - You can check that, for example with:
    ```bash
    gcc --version
    ```
    - Since the `flag_tool` is a C program, you have to compile it again:
      * `flag_tool` includes `sqlite3.h`, which is likely not yet installed on your system.
      * It can be installed (together with the required shared library) via:
      ```bash
      sudo apt install libsqlite3-dev
      ```
  * To work with the database that you downloaded from the server, you likely need [`sqlite3`](https://sqlite.org/index.html) ((`apt search sqlite3`))
    - To inspect the database file while refactoring, you might want to use a tool to "look into" your database file, such as the [DB Browser for SQLite](https://sqlitebrowser.org/), which you can install via:
   ```bash
   sudo apt install sqlitebrowser
   ```

### How do I start refactoring _ITU-MiniTwit_?

Your task is to modify as few lines as possible in the given sources of _ITU-MiniTwit_, just enough to make it run on your Linux system with a Python >= 3.12 and the dependencies given above.

  * You will likely want to make use of the tool `2to3`, which is part of your Python installation, and which can help you translating Python 2 programs to Python 3 programs.
    - You might want to read its help text before using it:
    ```bash
    2to3 --help
    ```
    - After applying the `2to3` tool compare the original source code of `minitwit.py`, i.e., the one that you downloaded in class from the old server, with the `minitwit.py3` that is generated by the tool.
      - You can compare text files with the `diff` command:
      ```bash
      diff minitwit.py minitwit.py3
      ```
      - Once you are sure that you understand what the `2to3` tool changed, replace the contents of `minitwit.py` with the Python 3 sources.
  * After refactoring `minitwit.py` to a modern Python 3 version, do the same refactoring with `minitwit_tests.py`.
    That is, make sure that the tests that can be executed against the original version of `minitwit.py` pass against your refactored version of `minitwit.py` too.
    **OBS**: Making use of existing test suites during refactoring is one of the most important tasks in software evolution.

  * **Hint**:
    - When converting `minitwit.py` to Python 3 you might receive an error when reading the SQL script when initializing the database in line: `db.cursor().executescript(f.read())`.
      Likely, decoding of the file contents into `utf-8` has to be declared explicitly.
    - Make sure to test this code (by running it), which will only be executed when initializing an empty database.
    - Also some functions from the `werkzeug` module were moved to another submodule. To resolve the issue Google for the error message and you will find a corresponding change entry.

  * For information, check the runtime dependencies of your compiled `flag_tool` with the `ldd` command:
    ```bash
    ldd ~/Desktop/itu-minitwit/flag_tool
    ```
  * Lastly, adapt the shell script `control.sh` according to the recommendations of the tool [`shellcheck`](https://www.shellcheck.net/), which is a linter for shell scripts
    ```bash
    shellcheck control.sh
    ```
    - You can install the tool via: `sudo apt install shellcheck`

## 4) Share your Work on GitHub

  - Create a public repository on GitHub (**Not on github.itu.dk but on github.com**).
    - Either create an organization for all your team members and let the organization own all repositories that you create during this semester,
    - or, create a public repository for one of you and invite the other team members as collaborators.
  - Keep versions of all your refactoring work in that repository.
  - Once you are done (and latest by **Thursday Feb 5th, at 12:00**) [create a release](https://help.github.com/en/github/administering-a-repository/creating-releases) with your refactored version of _ITU-MiniTwit_.


Please share your repositories with us. Send a GitHub pull-request on the file [`repositories.py`](https://github.com/itu-devops/MSc_lecture_notes/blob/master/repositories.py) in which you replace, e.g., `https://github.com/<gh_id>/<proj_id>` with the repository URL of your group. In case you use more than one repository, please add them to the corresponding list too.

##### Pull request???

In case you are in doubt about how to send a pull request on GitHub, see:

  * https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
  * https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project


## 5) Preparation for next time

Read and work through the [preparation material](../session_02/README_PREP.md) before the next session, I will refer to some of it's contents during the lecture.

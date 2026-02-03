-----------


# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [1) Replace _ITU-MiniTwit_ with C♯ ASP.Net _Chirp_ application.](#1-replace-itu-minitwit-with-c-asp.net-chirp-application)
  - [2) Containerize _ITU-MiniTwit_ with Docker.](#2-containerize-itu-minitwit-with-docker)
  - [3) Preparation for next time](#3-preparation-for-next-time)



## 1) Replace _ITU-MiniTwit_ with C♯ ASP.Net _Chirp_ application

### Groups with access to a C♯ ASP.Net _Chirp_ application

If you took BDSA earlier and you built a _Chirp_ application in that course, replace the legacy Python _ITU-MiniTwit_ application with your _Chirp_ application.
Your _Chirp_ application switches name and is called _ITU-MiniTwit_ from now on.
Refactor your application so that logins without Github OAuth are possible similar to the previous Python-based _ITU-MiniTwit_ application.

That is:
  - Remove the "login via GitHub" functionality.
  - Add instead login functionality as in the original _ITU-MiniTwit_ application.
    That is, use HTTP Session cookies to handle if a user is logged into your system.
  - Likely, [this documentation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/app-state?view=aspnetcore-8.0) helps you to get started.


### Groups without access to a C♯ ASP.Net _Chirp_ application

In case you are a group in which nobody built a _Chirp_ application in BDSA, then continue to use the Python Flask application in a modern up-to-date environment.
That might be the case for data science or exchange students.

### For all

Create a new *release* with a first version of your replaced _ITU-MiniTwit_ application, latest by **Monday, Feb. 9th, at 12:00**)


## Guidelines for using AI code assistants like GitHub Copilot, ChatGPT, etc.

In case you use AI code assistants, you have to do the following:

  - Check that what these systems suggest you to do is in line with what you actually want to do.
  - Add `GitHub Copilot`, `ChatGPT`, etc. as co-author to all commits in which you incorporate their work.
    See [this documentation](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) for how to do it.
  - Please keep a log with your experiences of using such systems and share your experiences with us.
  - Only commit code that you actually understand.


## 2) Containerize _ITU-MiniTwit_ with Docker

Use Docker to containerize your _ITU-MiniTwit_ application.
That is, create respective Dockerfiles (and if needed yet Docker Compose files) in your repository.
These containerize your application and allow all team members to develop your application in a uniform environment.


## 3) Preparation for next time

Please [setup the tools needed for the next session](../session_03/README_PREP.md).

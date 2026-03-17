-----------

# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [0) Add tests to your CI chain](#0-add-tests-to-your-ci-chain)
  - [1) Enhance your CI Pipelines with at least three static analysis tools](#2-enhance-your-ci-pipelines-with-at-least-three-static-analysis-tools)
  - [2) Add Maintainability and Technical Debt estimation tools to your projects](#1-add-maintainability-and-technical-debt-estimation-tools-to-your-projects)
  - [3) Software Maintenance](#3-software-maintenance)


## 0) Add tests to your CI chain

Add integration tests, UI, and end-to-end tests to your CI chains.
For example, adapt the test case `test_itu_minitwit_ui.py`, from the lecture and exercise material, so that it can be executed from within a Docker container.
Add a respective setup, e.g., via `docker compose` to your CI chains.
Reuse the tests that you took over earlier, i.e., the integration test from the initial application and the API test from session 3.

Use the test suite as a _quality gate_. That is, in case tests do not pass, stop delivery and deployment of your systems.
You might want to start with integrating the API test that you received in session 3 and the end-to-end test and UI test that you received in the lecture material.


## 1) Enhance your CI Pipelines with at least three static analysis tools


Include linters and code formatters for the programming and configurations that you are using in your repositories.
That is, you likely include at least three static analysis tools as software quality gates into your CI/CD pipelines.
One linter and one code formatter for your main programming language, one linter for your Dockerfiles.
Add other suitable linters, e.g., in case you rely on shell scripts `shellcheck`, etc.
You might want to start searching for relevant tools for your respective languages and frameworks here: https://github.com/mre/awesome-static-analysis.

Include all of these tools in a way that you either abort build in case quality of your code is too low (you will have to define some threshold here) or that you decide to trust them and let the tools try to automatically fix problems (in case you find a tool that supports that).
In the latter case, you want to let the corresponding tool contribute the applied changes back to the corresponding source repository.



## 2) Add Maintainability and Technical Debt estimation tools to your projects

Add the following two tools to your projects:

  * [Sonarqube](https://sonarcloud.io)
    - After doing the exercises you should already have done this.
  * [Codacy](https://www.codacy.com)

The task should be easy and quick to perform.
You can login via GitHub to the two tools and just select the corresponding repository/-ies.

React on the issues that these tools are 'complaining' about.
You do not have to fix everything.
But prominent issues that you agree on, should be fixed from now on.
Be aware of that the tools automatically analyze new versions of your projects, i.e., check that your future work does not introduce new issues and decreases the quality metrics.


## 4) Software Maintenance


We are in software maintenance. That is, fix issues of your version of _ITU-MiniTwit_ **as soon as possible**. Let's say that as soon as possible means within 24 hours if possible, i.e., if it is not a super big issue that requires a big rewrite.

Now, with your monitoring systems in place, you will likely observe issues when they arise or even before the arise. Just fix them as soon as you realize them.

Additionally, our dashboards illustrate status and potential errors as the simulator 'sees' them [here](http://64.226.108.122/status.html). For example, fix wrong status codes, e.g., `tweet` shall return `204` instead of `200`, or too slow response times.

Continue to release (now likely automatically) at least once per week versions of your system with corresponding fixes.



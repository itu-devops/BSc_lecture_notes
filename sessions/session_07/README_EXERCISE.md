### Your Turn!
<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>


#### Run the UI and the end-to-end test from the lecture material

Next to the lecture material, you received an example of a UI and end-to-end test for the _ITU-MiniTwit_ application in the file `test_itu_minitwit_ui.py`.

The purpose of this exercise is to make that test run on a given _ITU-MiniTwit_ application.
To do so, the following dependencies have to be setup:

  * `pip install selenium`
  * `pip install pymongo`
  * `pip install pytest`
  * The Firefox webbrowser (`sudo apt install firefox`)
  * A so-called driver, which is a progam that can control Firefox programatically:
    `wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz`
    The example assumes that the driveer is downloaded and extracted to the same directory that contains the test `test_itu_minitwit_ui.py` .
  * `tar xzvf geckodriver-v0.32.0-linux64.tar.gz`
  * After extraction, the downloaded artifact can be removed: `rm geckodriver-v0.32.0-linux64.tar.gz`

The application that it tests is the version of _ITU-MiniTwit_ that you got to know during the exercises on Docker:
https://github.com/itu-devops/flask-minitwit-mongodb/tree/Containerize (*OBS*: branch Containerize)

```bash
$ git clone https://github.com/HelgeCPH/flask-minitwit-mongodb.git
$ cd flask-minitwit-mongodb
$ git switch Containerize
```

After editing the `docker-compose.yml` file file where you replace `youruser` with your respective username, the
application can be started with `docker compose up`.

Now, the test itself can be executed via: `pytest test_itu_minitwit_ui.py`.

In its current configuration, the tests are executed in `headless` mode, i.e., no browser is visible.
Such test can be executed in CI chains within Docker containers too, which usually do not have a display configured.

In case you want to observe the test to run in a visible browser, uncomment lines 69 and 87 in `test_itu_minitwit_ui.py`.
Per default, Selenium test are executed in a visible browser, which is what these two line regenerate again.


#### Analyze software quality and technical debt with SonarQube

Analyze software quality and technical debt of your _ITU-MiniTwit_ application with [SonarQube](https://www.sonarqube.org/) ([SonarCloud](https://sonarcloud.io/) is a readily available hosted version of SonarQube). Do the following once per group:

  * Navigate to https://sonarcloud.io/
  * Login via GitHub
  * Add a new project by clicking the `+` sign on the top right of the window followed by `Analyze new project`
  * And select the repository or the repositories that you want to assess.

After the analysis is complete, try to understand with the [documentation](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#header-4) and if necessary with [Letouzey _"The SQALE method for evaluating technical debt"_](https://www.researchgate.net/profile/Jean_Louis_Letouzey/publication/239763591_The_SQALE_method_for_evaluating_Technical_Debt/links/0c9605357748774a21000000/The-SQALE-method-for-evaluating-Technical-Debt.pdf) what is presented as technical debt. Does that correspond to your understanding of technical debt?


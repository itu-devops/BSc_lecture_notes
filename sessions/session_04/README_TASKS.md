-----------


# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [1) Complete implementing an API for the simulator in your ITU-MiniTwit.](#1\)-Complete-implementing-an-API-for-the-simulator-in-your-ITU-MiniTwit.)
  - [2) Creating a CI/CD setup for your ITU-MiniTwit.](#2\)-Creating-a-CI/CD-setup-for-your-ITU-MiniTwit.)


## 1) Complete implementing an API for the simulator in your _ITU-MiniTwit_.


Next week, we will start a simulator that will run until the end of this course. It will simulate users using your micro-blogging platform.

You can find the specification for the simulator API in [`../session_03/API_Spec/`](../session_03/API_Spec/).
**OBS**: your applications have to:

  - provide the same end points (on different hosts of course and potentially different ports),
  - ingest the same HTTP requests, i.e., GETs and POSTs as specified with the same parameters and payloads as provided,
  - provide at least the same HTTP status codes in response as specified.

A corresponding test (`API_Spec/minitwit_sim_api_test.py`) illustrates how the simulator requests will be formed. You can inspect it and run it via `pytest minitwit_sim_api_test.py`.

Next to the unit test, there is a small program with some more test data, which is similar to the simulator program that will run against your systems. It is located in [`../session_03/API_Spec/minitwit_simulator.py`](../session_03/API_Spec/minitwit_simulator.py) and can be run via:

```bash
$ python minitwit_simulator.py http://localhost:5001
```

where the argument `http://localhost:5001` has to be replaced with the URL of where you simulator API is running. In case this simulator test does not log any errors, you should be all fine for next week. If errors are logged, you have to likely fix the corresponding issue either in your implementation of the simulator API or in the implementation of your version of _ITU-MiniTwit_.


## 2) Creating a CI/CD setup for your _ITU-MiniTwit_.


Until next week, create a CI/CD setup for your _ITU-MiniTwit_ development.

  * You can freely choose your CI/CD system. Likely adapting the example [`today's exercises`](README_EXERCISE.md) is most time efficient.
  * For now, you choose freely if you want to go for continuous delivery or continuous deployment.
  * Let your build pipeline contain not only building your application but also execution of your test suite and other appropriate build stages.

From now on, create the (at least weekly) releases on GitHub automatically. Release the version of your _ITU-MiniTwit_ that is deployed to and running in production.

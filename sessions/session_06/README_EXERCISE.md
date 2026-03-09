### Your Turn!
<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>


#### A) Replicate the Monitoring Setup from Class

  - Navigate to https://github.com/itu-devops/itu-minitwit-monitoring and clone the repository with its two branches to your computer.
  - Start by inspecting and running the application in the master branch. It contains the containerized _ITU-MiniTwit_ with monitoring in the exact same way as discussed in class.
  - Bring-up and run the application with monitoring enabled as described in the main [`README.md`](https://github.com/itu-devops/itu-minitwit-monitoring/blob/master/README.md)


#### B) Identifying Refactoring Candidates with Monitoring

  - After you developed with your group mates an understanding of how the given _ITU-MiniTwit_ differs from earlier versions (for example the one that you overtook in session 1) do the following:
    - Switch to branch `function_counters`
    - Rebuild the main application image (`webserver`)
    - Observe via the Prometheus metrics, the Prometheus dashboard or via Grafana, which functions are executed by the simulation program, see [`minitwit_client_sim.py`](https://github.com/itu-devops/itu-minitwit-monitoring/blob/function_counters/minitwit_client_sim.py).
    - Can you identify a potential refactoring candidate in `minitwit.py` based on the function call frequencies (stored in metric `minitwit_fct_*`)?

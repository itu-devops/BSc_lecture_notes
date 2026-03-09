-----------


# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [1) Add Monitoring to Your Systems](#1-add-monitoring-to-your-systems)
  - [2) Migrate to Another Database](#2-migrate-to-another-database)
  - [3) Software Maintenance](#3-software-maintenance)


## 1) Add Monitoring to Your Systems

Your task until next week is to add monitoring to your _ITU-MiniTwit_ systems.
For sure, add application monitoring and infrastructure monitoring.
Add all other categories of monitoring after your liking and after what you deem important for your application.

In case you adapt the monitoring example from class (https://github.com/itu-devops/itu-minitwit-monitoring), make sure to turn your Grafana configuration/dashboard into code as illustrated in the given example.
Later, you do not want have to click together your dashboards and visualizations every time you restart the Grafana container. To do so, you may start reading:

  * https://grafana.com/docs/grafana/latest/installation/configure-docker/
  * https://runkiss.blogspot.com/2020/01/using-prometheus-grafana-to-monitor.html

Add a link to your monitoring dashboard via a pull request to the file [`misc_urls.py`](https://github.com/itu-devops/BSc_lecture_notes/blob/master/misc_urls.py) in https://github.com/itu-devops/BSc_lecture_notes. (Replace the URL `"http(s)://<TBA>/"` below the comment `# Monitoring URL:` with your respective URL.
Link either a read-only dashboard or add a user with name and credentials that Helge provides you via the Teams chat channel, so that we can see what you are monitoring and can provide feedback on it in the start of the next session.


## 2) Migrate to Another Database

Migrate your application's database away from SQLite.
You can either self-host a database (likely having it on a separate VPS is a good idea), or you can "buy" one of DigitalOceans or other vendors' managed databases.

For this task it is good enough to perform a migration in which you will "loose" some of the simulator requests due to a short amount of downtime while switching the application to the new database.
However, try to minimize the amount of downtime for database migration.

If you have a lot of energy and time left, you might want to try to implement a zero-downtime migration with redundant systems.
This requires quite a bit of oumph and strategic thinking.
Therefore, only go for it when you have a lot of time and energy.


## 3) Software Maintenance

From now on, we are in software maintenance. That is, fix issues of your version of _ITU-MiniTwit_ **as soon as possible**. Let's say that as soon as possible means within 24 hours if possible, i.e., if it is not a super big issue that requires a big rewrite.

Likely, after the simulator is started you will experience some issues in your systems. Just fix them as soon as you realize them.

For example, you will be able to see status and potential errors as the simulator 'sees' them [here](http://64.226.108.122/status.html).

Continue to release, now automatically, at least once per week versions of your system with corresponding fixes.

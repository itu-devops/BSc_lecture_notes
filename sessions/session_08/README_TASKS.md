-----------

# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [1) Add Logging to Your Systems](#1-add-logging-to-your-systems)
  - [2) Improve Logging of Your Systems Over Time](#2-improve-logging-of-your-systems-over-time)
  - [3) Software Maintenance](#3-software-maintenance)



## 1) Add Logging to Your Systems

Until next week, add logging to your _ITU-MiniTwit_ systems.

You can deploy a Grafana Loki stack as we have [shown in the exercises](https://github.com/itu-devops/itu-minitwit-logging/tree/grafana_loki); but you can use also another logging stack.
In case you are choosing a Grafana Loki logging stack, make sure to replace the end-of-lifed (EOL) Promtail tool with [Grafana Alloy](https://grafana.com/docs/alloy/latest/introduction/).

Please share your logging dashboards with us, similar to your monitoring dashboards.
Add the URL of your logging dashboard to the `"Logging URL"` section of the `misc_urls.py` file.
Make it accessible with the same credentials as the monitoring dashboard.

In case you adapt the logging example from [class](https://github.com/itu-devops/itu-minitwit-logging/tree/grafana_loki), make sure to turn your Grafana configuration/dashboard into code.
Later, you do not want have to click together your dashboards and visualizations every time you restart the Grafana container.


## 2) Improve Logging of Your Systems Over Time

In case you experience issues with your systems, try to resolve them with the information that you gather from your logs.
Likely, you will realize that certain information is missing from your logs.
Whenever you experience the lack of information in logs that would be required to resolve an issue, then improve logging over time.


When resolving issues, keep a log for humans (like a diary) containing what you have done to fix issues with logging. That will come in handy later, when writing your reports.


## 3) Software Maintenance


We are in software maintenance. That is, fix issues of your version of _ITU-MiniTwit_ **as soon as possible**. Let's say that as soon as possible means within 24 hours if possible, i.e., if it is not a super big issue that requires a big rewrite.

Now, with your monitoring systems in place, you will likely observe issues when they arise or even before the arise. Just fix them as soon as you realize them.

Additionally, our dashboards illustrate status and potential errors as the simulator 'sees' them [here](http://64.226.108.122/status.html). For example, fix wrong status codes, e.g., `tweet` shall return `204` instead of `200`, or too slow response times.

Continue to release (now likely automatically) at least once per week versions of your system with corresponding fixes.

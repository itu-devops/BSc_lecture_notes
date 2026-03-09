-----------


# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [1) The Simulator starts today!](#1-the-simulator-starts-today)
  - [2) DevOps Principles](#2-devops-principles)
  - [3) Make your configuration management scripts idempotent](#3-make-your-configuration-management-scripts-idempotent)
  - [4) Software Maintenance](#4-software-maintenance)


## 1) The Simulator starts today!

We will start the simulator **today** in the exercise session (in between 11:00 and 12:00).

In case you have not done so yet, send a pull request to `repositories.py` in our central repository: https://github.com/itu-devops/BSc_lecture_notes/blob/master/repositories.py!

Add two URLs:

  * One to your running applications (edit `"http://<minitwit_application_url>"`)
  * Another one to the simulator API endpoint (edit `"http://<sim_api_url>"`)


## 2) DevOps Principles

Consider how much you as a group adhere to the "*Three Ways*" characterizing DevOps (from _"The DevOps Handbook"_):

  * Flow
  * Feedback
  * Continual Learning and Experimentation

Map what you are doing with regards to each principle.
In case you realize you are not doing something for a principle change the way you are working as a group accordingly.


## 3) Make your configuration management scripts idempotent

Make sure that all configuration management code is idempotent, i.e., it can be run repeatedly without undesired side-effects leaving your systems in undesired states.

Optionally, if you consider that configuration management tools like Ansible, Chef, Puppet, etc. are more suitable than plain shell scripts, migrate your configuration management code to one of these.
In the following, you find a list of potential alternative configuration management tools:

  * [Ansible](https://docs.ansible.com/projects/ansible/latest)
  * [Chef](https://docs.chef.io/)
  * [Puppet](https://www.puppet.com/docs/index.html)
  * [Salt](https://docs.saltproject.io/en/latest/contents.html)
  * [PyInfra](https://docs.pyinfra.com/en/3.x/)
  * [Pulumi](https://www.pulumi.com/docs/)


## 4) Software Maintenance

From now on we are in software maintenance. That is, fix issues of your version of _ITU-MiniTwit_ as soon as possible. Likely, after the simulator started, you will experience some issues in your systems. Just fix them as soon as you realize them.

For example, you will be able to see status and potential errors as the simulator 'sees' them [here](http://209.38.211.172/status.html).

Continue to release (now likely automatically) whenever new features and bug-fixes are ready (least once per week).

# Your turn now!

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>

  - [1) Implement an API for the simulator in your _ITU-MiniTwit_.](#1-implement-an-api-for-the-simulator-in-your-itu-minitwit)
  - [2) Continue refactoring of your ITU-MiniTwit.](#2-deploy-your-itu-minitwit)


## 1) Implement an API for the simulator in your _ITU-MiniTwit_.


In two weeks, we will start a simulator that will run until the end of this course. It will simulate users interacting with your micro-blogging platform.

You can find a specification of the required simulator API [here](./API_Spec/swagger3.json).
A detailed explanation of how to use this simulator API specification can be found [here](./API_Spec/README.md).

In essence, we need to make sure that the simulator can interact with your applications.
That is, we have to make sure that all of your _ITU-MiniTwit_ provide the endpoints, can handle payloads, and return HTTP status codes, in the way the simulator expects it.
By implementing this interface

To double check that you implemented the interface correctly, we provide you corresponding API tests ([`API_Spec/minitwit_sim_api_test.py`](./API_Spec/minitwit_sim_api_test.py)).
It illustrates how the simulator requests will be formed.
You can inspect it and run it via `pytest minitwit_sim_api_test.py` against your simulator APIs.
(`pytest` can be installed via `pip`)

Next to the API tests, we provide you a basic program and data, which is very similar to the simulator that we will run against your systems.
It is located in [`API_Spec/minitwit_simulator.py`](API_Spec/minitwit_simulator.py) and can be run via:

```bash
$ python minitwit_simulator.py http://localhost:5001
```

where the argument `http://localhost:5001` has to be replaced with the URL of your simulator API.
In case this simulator test does not log any errors, you should be all fine for simulator start in two weeks.
If errors are logged, you have to fix the corresponding issue either in your implementation of the simulator API or in the implementation of your version of _ITU-MiniTwit_.


| :exclamation:  **OBS**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| We are talking about an API specification here. It is completely up to you how you integrate this into your systems. That is, that the program in `API_Spec/minitwit_sim_api.py` interacts directly with the database is only for illustration. It does not mean that the API has to be implemented like that in your systems! You will very likely want to factor out the common behavior between your endpoints that handle our simulator and your endpoints that render HTML. |


## 2) Deploy your _ITU-MiniTwit_.

### a) Create a virtual machine for your _ITU-MiniTwit_ in "the cloud"

Create a virtual machine for your _ITU-MiniTwit_ in "the cloud".
You might want to create a virtual machine on DigitalOcean, where you get free credits from the GitHub education pack.
Since DigitalOcean is a US American cloud provider and for digital sovereignty, you might consider a European alternative to DigitalOcean, see e.g., [here](https://european-alternatives.eu/alternative-to/digitalocean) or [here](https://www.hetzner.com/cloud/).
When searching for an alternative provider, you are searching one that offers virtual private servers (VPS).
If you want to experiment with full digital sovereignty, you might want setup a physical server, e.g., a small Raspberry Pi, at home.

In essence, You are free to deploy to whichever Infrastructure-as-a-Service (IaaS) provider of your choice or your own servers.
That is, **do not** deploy to a Platform-as-a-Service, like Heroku, Google App-Engine, Azure App Service, etc.

Encode your virtual machine creation. That is, create either a Vagrantfile, a shell script, etc. that creates the VM for you.
In case you provision a physical server, keep a log that encodes every step necessary to setup the server, this is your IaC for humans in this case.
Version control your infrastructure creation code in your Git repository.
That means, creation of your virtual machines has to be automatically reproducible, i.e., no clicking in UIs required.

#### Hints

    - You might want to start with the exercise from the demo in the lecture
      * For a setup with Vagrant, see slide [7) Automatic provision of remote clusters of virtual machines at DigitalOcean via Vagrant](./Slides.html#37).
      * For a setup via a shell script see slide [6) Automatic provision of remote virtual machines at DigitalOcean via a web-API](./Slides.html#34)
      * For a setup via Ruby/Python script see slide [6) Automatic provision of remote virtual machines at DigitalOcean via a web-API (contd.)](./Slides.html#36)
    - That is, **do not** provision VMs manually, instead use a corresponding *script*, `Vagrantfile`, or a similar reproducible setup for that task.
    - To make future operations more smooth, you might **consider to use a [floating IP](https://docs.digitalocean.com/products/networking/floating-ips/) 'infront' of your server**, see the [API spec.](https://docs.digitalocean.com/reference/api/digitalocean/#tag/Floating-IPs) for receiving one.
    - Make your development environment and deployment environment "look alike". That is, you develop on an Ubuntu 22.04 based Linux (Pop!_OS), choose the same environment for your remote server(s).
    - Make sure to not share any API keys or access tokens in your public repository.


### b) Release and deploy your _ITU-MiniTwit_.

  * Prepare a new release of your _ITU-MiniTwit_ latest by **Monday Feb 16th, at 12:00**)
  * Via a script, deploy your application, the release from above, to you server.
    - **OBS**: The simulator API from the task 1 is part of your _ITU-MiniTwit_, i.e., it has to be deployed too.
  * Your application has to be reachable via a public IP/domain.

  * Once, your application is deployed and running, send a pull request to `repositories.py` in our central repository: https://github.com/itu-devops/BSc_lecture_notes/blob/master/repositories.py
    - Add two URLs:
      * One to your running applications (edit `"http://<minitwit_application_url>"`)
      * Another one to the simulator API endpoint (edit `"http://<sim_api_url>"`)


### c) Release and deploy your _ITU-MiniTwit_.

Document in the README.md file in the root of your repository the steps from task 2 a) and b).
That is, it should be documented how to come from cloning your repository to a fully deployed _ITU-MiniTwit_ application.
So you want to document how to create the VM and how to deploy a release to it.
In the best case, your documentation consists of two main commands:

```bash
$ git clone git@github.com:<your_id>/<your_repo>.git
$ ./provision_itu_minitwit.sh  # or just: vagrant up
```

Of course, you likely want to document which secrets have to be configured on the computer that runs the provisioning command.
Over the course of the project, keep the documentation, the provisioning code, and the actual application in sync.

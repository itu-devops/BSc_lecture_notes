# Exercises

<img src="https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif" width=50%/>


## A deeper dive into Vagrant with a **remote** development scenario

  - To make this example work properly, you have to have a pair of SSH keys. In case you do not have them set up yet see [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804) for how to do this.

  - It is assumed that your SSH keys are located in your home directory in the hidden directory `~/.ssh/id_rsa` (hidden directories and files are marked by a leading `.`). In case you have them stored somewhere else, you have to modify the line `config.ssh.private_key_path = '~/.ssh/id_rsa'` in the given `Vagrantfile accordingly.
  - You have to be registered at DigitalOcean (remember to use your free credit from the [Github education pack](https://education.github.com/pack)).
  - [Your public SSH key has to be registered at DigitalOcean](https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/to-account/)

  - Additionally, you have to have two environment variables set. One `$SSH_KEY_NAME` which is the name of the key that you have registered at DigitalOcean's homepage. Furthermore, the `Vagrantfile` assumes that you have set the environment variable `$DIGITAL_OCEAN_TOKEN` to the API token, which you receive from DigitalOcean, see [this tutorial](https://www.digitalocean.com/docs/api/create-personal-access-token/)
    - In case you are wondering about setting environment variables, [read this StackOverflow answer for help](https://askubuntu.com/a/58828).

  - Lastly, you need to have the DigitalOcean Vagrant Provider installed. If you have not installed it yet, do so:

```bash
$ vagrant plugin install vagrant-digitalocean
```

Now, switch to the branch `VMify_remote` of the example repository.
Check if everything starts up correctly:


```bash
$ git clone https://github.com/itu-devops/flask-minitwit-mongodb.git
$ cd flask-minitwit-mongodb
$ git checkout VMify_remote
$ rm -r .vagrant/ db_ip.txt
$ vagrant up
==> webserver: Running action triggers before up ...
==> webserver: Running trigger...
==> webserver: Waiting to create server until dbserver's IP is available.
==> dbserver: Using existing SSH key: ITU
==> dbserver: Creating a new droplet...
...
==> dbserver: Writing dbserver's IP to file...
Now, I have it...
...
==> webserver: Using existing SSH key: ITU
==> webserver: Creating a new droplet...
==> webserver: Assigned IP address: <public_ip_address>
...
```

While waiting, make sure you understand the `Vagrantfile` for remote deployment.
In case you are in doubt about anything check the [brief and really good documentation](https://www.vagrantup.com/docs/).
In particular, make sure to understand how the VMs are created in order (first `dbserver` and then `webserver`).

Take the public IP address of the webserver (marked in the output above as `<public_ip_address>`), and navigate with your browser to http://<public_ip_address>:5000.
Make sure that you can see the public timeline of _ITU-MiniTwit_.

Experiment with SSHing into the two remote machines via `vagrant ssh dbserver` and `vagrant ssh webserver` respectively.

Once you are done experimenting with the two virtual machines, make sure to destroy that setup again by running `vagrant destroy`. It will prompt you to verify destruction of both VMs. If you do not destroy them the VMs will continue to exist and you will be billed for them accordingly.




## Getting accustomed to `Vagrantfile`s

  * Take the local development scenario from https://github.com/HelgeCPH/flask-minitwit-mongodb/tree/VMify_local (branch **`VMify_local`**).
  * Add a third **local** virtual machine with the IP `192.168.20.4`. It will serve as a client (give it a corresponding name in the `Vagrantfile`.
  * Let it be a machine with the same Ubuntu installation.
  * On it, install via the machines provision script a text-based browser, such as, `lynx` or `w3m`.
  * After provisioning of the three local VMs, ssh into your client machine.
  * With the text-based browser, connect to http://192.168.20.3:5000.
  * Verify that you get the public timeline of _ITU-MiniTwit_ displayed.

In case you can see the public time line of the _ITU-MiniTwit_ clone.


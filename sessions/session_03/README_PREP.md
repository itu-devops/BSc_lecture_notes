# Preparation Material for Session 03

Install VirtualBox and Vagrant on your computer.


### Vagrant & VirtualBox

**Note:** VirtualBox cannot be run in a VirtualBox VM. Since we are using Vagrant here to provide VirtualBox virtual machines, it means that you should install Vagrant and related plugins directly in your host OS (Windows/MacOS) if you are running Linux in a virtual machine already.


#### Install the Hypervisor (VirtualBox) in Linux

To install VirtualBox you can use sudo:

```bash
sudo apt install virtualbox virtualbox-ext-pack
```

In case you observe an error about a package conflict to `virtualbox-7.2` or similar, then try to remove the previously installed VirtualBox packages (`sudo apt remove virtualbox virtualbox-ext-pack`) first and then re-install them as above.

#### Install Vagrant

Since the packaged Vagrant in the linked repositories is in a bit buggy version we install it directly from the package provided by the tool vendor:

```bash
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant
```

#### Install Vagrant Plugins

After installing Vagrant, we need to install a VirtualBox plugin that we will need later:
```bash
vagrant plugin install vagrant-vbguest
```

We install a few other useful plugins:

```bash
vagrant plugin install vagrant-digitalocean
vagrant plugin install vagrant-scp
vagrant plugin install vagrant-reload
```

If you're using VirtualBox save the following into a file called `Vagrantfile` in your current directory :

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-22.04"

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
end
```

Now, run from your current directory (the one in which you saved the `Vagrantfile`):

```bash
vagrant up
```


The command downloads the OS image specified in the configuration and brings up a virtual machine on your computer (with the specified hypervisor as backend).
It will take some time since the corresponding OS image has to be downloaded first. That image will be cached on your disk, i.e., following VM instantiations of the same image will be faster.
Observe that no error message is displayed. If so, and in case you cannot find a solution for it, we will look at it in class.

Maybe, you observe an error like the following:

```
/home/user/.vagrant.d/gems/3.3.6/gems/vagrant-vbguest-0.32.0/lib/vagrant-vbguest/hosts/virtualbox.rb:84:in `block in guess_local_iso': undefined method `exists?' for class File (NoMethodError)

            path && File.exists?(path)
                        ^^^^^^^^
Did you mean?  exist?
```

To fix it, we apply a hack. We fix the syntax error in the respective Ruby file in-place.
Run the following command only once (if in doubt about its meaning, read the man page of `sed`):

```bash
$ sed -ie 's/File.exists?(path)/File.exist?(path)/g' ~/.vagrant.d/gems/3.3.6/gems/vagrant-vbguest-0.32.0/lib/vagrant-vbguest/hosts/virtualbox.rb
```

Now, you can run `$ vagrant up` again and the example should start up without any error.

If you wanted to fix the reason for the error without applying a hack, you would have to do the following:

  - Identify the cause of the error, e.g., via [the issue tracker of Vagrant](https://github.com/hashicorp/vagrant/issues/13404)
    - There you realize that the issue stems not from the Vagrant tool but from the `vagrant-vbguest` plugin.
    - You realize that the [original plugin (latest version 0.32.0) is not maintained anymore](https://github.com/dotless-de/vagrant-vbguest).
  - However, somebody [forked the `vagrant-vbguest` plugin](https://github.com/dheerapat/vagrant-vbguest) and fixed the error.
  - To get, build, and install the updated version in the fork the `vagrant-vbguest` plugin you have to do the following:
  ```bash
  $ https://github.com/dheerapat/vagrant-vbguest.git
  $ cd vagrant-vbguest.git
  $ gem build vagrant-vbguest.gemspec
  $ vagrant plugin install vagrant-vbguest-0.32.1.gem
  ```

After all the work above and after creating a local VM without any error message, for now, you can run delete the virtual machine with the following command:

```bash
vagrant destroy
```

### Intro to VMs with Vagrant

  > Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.
  >
  > Vagrant provides easy to configure, reproducible, and portable work environments built on top of industry-standard technology and controlled by a single consistent workflow to help maximize the productivity and flexibility of you and your team.
  >
  > https://www.vagrantup.com

In case you are in doubt about anything in the following quick intro, check the [brief and really good documentation](https://www.vagrantup.com/docs/).

#### Initialize & Start a VM

You can start your setup by creating a `Vagrantfile`. The argument to `vagrant init` is the name of the *box*. That is,

```bash
$ mkdir vm
$ cd vm
$ vagrant init bento/ubuntu-22.04
$ vagrant up
```

  > After running the above commands, you will have a fully functional VM in VirtualBox running Ubuntu. You can SSH into this machine with `vagrant ssh`, and when you are done playing around, you can terminate the virtual machine with `vagrant destroy`.




#### Accessing a VM

You log onto a VM with SSH as in the following.

```bash
$ vagrant ssh
```

You can leave the guest VM with:

```bash
$ vagrant@vagrant: exit
```

#### Teardown

A running VM can be ...

  * put to sleep

  ```bash
  $ vagrant suspend
  ```

  * turned off

  ```bash
  $ vagrant halt
  ```

  * removed completely

  ```bash
  $ vagrant destroy
  ```

#### State of VMs

The following command will display a list of all VMs and their respective states, i.e., `saved`, `poweroff`, `active`, etc.

```bash
$ vagrant global-status
```

#### VMs with other Operating Systems

That is, you can quickly setup development environments for many operating systems. For example, in the following the initialization and use of a FreeBSD and Windows VM.

```bash
$ mkdir vm_freebsd
$ cd vm_freebsd
$ vagrant init bento/freebsd-14
$ vagrant up
```

```bash
$ mkdir vm_win
$ cd vm
$ vagrant init stromweld/windows-11
$ vagrant up
```

You can find a catalog of available boxes at https://app.vagrantup.com/boxes/search

<img src="images/vm_catalogue.png" width="80%">


### Vagrant for **local** development setup

At last, apply `vagrant` for a usual scenario: reproduction of development environments.

The branch [`VMify_local`](https://github.com/itu-devops/flask-minitwit-mongodb/tree/VMify_local) of repository https://github.com/itu-devops/flask-minitwit-mongodb contains an _ITU-MiniTwit_ application similar to the one you took over last week. It was refactored to use a MongoDB database instead of an SQLite3 database.

The application is a two-layered application with a frontend server (called `webserver`) and a database server (called `dbserver`).
With the VM setup from the [`VMify_local`](https://github.com/itu-devops/flask-minitwit-mongodb/tree/VMify_local) branch, you have a complete running setup of the entire application that you can recreate on you computer, e.g., for local development.

To do so, clone the repository, switch to the right branch, check and try to develop a feeling for the contents of the [`Vagrantfile`](https://github.com/itu-devops/flask-minitwit-mongodb/blob/VMify_local/Vagrantfile), and start-up the VMs.

```bash
$ git clone https://github.com/itu-devops/flask-minitwit-mongodb.github
$ cd flask-minitwit-mongodb
$ git checkout VMify_local
$ vagrant up
Bringing machine 'dbserver' up with 'virtualbox' provider...
Bringing machine 'webserver' up with 'virtualbox' provider...
...
```

If everything starts error-free, you will find the running _ITU-MiniTwit_ at http://192.168.20.3:5000. With `vagrant ssh webserver` you can access the machine with the frontend code.


## Vagrant on other hosts (MacOS/Windows)

### MacOS

The following expects you to have the ["homebrew" package manager installed and setup](https://brew.sh/).


- Install VirtualBox:
```bash
brew install --cask virtualbox
```
- Install Vagrant as described on the [tool's documentation page](https://developer.hashicorp.com/vagrant/install).
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/hashicorp-vagrant
```
- Then continue installing the Vagrant plugins as described [above](#install-vagrant-plugins)

Note, in case you are on an ARM-based Mac, the virtual machines that you can use via virtualbox are all ARM-based too.
The reason is that VirtualBox is a hypervisor, not an emulator.
If you need to handle Intel/AMD-based virtual machines on such a Mac, then you have to switch to using a machine emulator, such as [`qemu`](https://www.qemu.org/).
Likely the easiest way to use `qemu` is via [UTM](https://mac.getutm.app/), which is an application that wraps `qemu`.

```bash
brew install --cask utm
```

You can use Vagrant with UTM too via the [respective provider](https://naveenrajm7.github.io/vagrant_utm/):
```bash
vagrant plugin install vagrant_utm
```


In case you decided earlier to rely on [VMWare Fusion to manage virtual machines on your Mac](https://dev.to/houssambourkane/run-vagrant-vms-in-a-m1m2m3-macos-chip-2p3l), you can use Vagrant with that too via the respective provider:
```bash
vagrant plugin install vagrant-vmware-desktop
```

### Windows

The following expects you to have the ["chocolatey" package manager installed and setup](https://chocolatey.org/install).

- Install VirtualBox:
```
choco install virtualbox
```
- Install Vagrant
```
choco install vagrant
```
- Then continue installing the Vagrant plugins as described [above](#install-vagrant-plugins)

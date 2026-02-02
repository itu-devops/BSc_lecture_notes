# Preparation Material for Session 02

## Version Control with Git

In case you did not configure your Git installation already, do so as described in [First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

In particular, configure your username, email address, and command line editor:

```bash
$ git config --global user.name "<Your Name>"
$ git config --global user.email <yourname>@itu.dk
```

In case you are not into using VI as editor, you might want to choose `nano`

```bash
$ git config --global core.editor nano
```

  * If you are rusty with basic Git concepts, like adding files to version control, viewing your commit history, undoing changes, etc., you might want to check chapter [2. Git Basics](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) from the Pro Git book.
  * Please read the following four sub-chapters of chapter [3. Git Branching on Git branches](https://git-scm.com/book/en/v2/)
    - [Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
    - [Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
    - [Branch Management](https://git-scm.com/book/en/v2/Git-Branching-Branch-Management)
    - [Remote Branches](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches)
  * To allow for a better understanding of why Git works the way it does read on [Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)

-------------------------------

## Setup Docker and Docker Compose 


Install Docker and Docker Compose to your computer.

The below is adapted from the official documentation for Ubuntu (updated for 2025): https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

### Docker

Uninstall old versions

```shell
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Install the docker repository for automatic updates
```shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install the following tools for docker

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Check if the Docker engine is up and running:

```bash
sudo systemctl status docker
```

or

```shell
sudo docker run hello-world
```

To be able to run docker commands as your current user, it has to be added to the respective group. (_notice some versions of the guide writes ${USER}, try this if the following doesn't work._)

```bash
sudo usermod -aG docker $USER
```

With the following, double check that your user is in the `docker` group.

```bash
su - $USER
id -nG
exit
```
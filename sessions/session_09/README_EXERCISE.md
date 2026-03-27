
## A Basic Reliable Web Service with Docker Swarm

Follow the following tutorial to deploy a Swarm


# Interactive 

### CLI Deployment of A Docker Swarm cluster on DigitalOcean


- create a new token 
![500](images/do_generating_token.png)

- Define the envvar: 
```
DIGITAL_OCEAN_TOKEN=blablabla
```
- Install the `jq`  command line tool if you don't already have it (e.g., `brew install jq` on a mac)
- [Upload](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/to-team/#upload-an-ssh-key-to-a-digitalocean-team-with-the-control-panel)  your SSH public key in DigitalOcean>Settings>Security


### New Docker Commands

  * `docker swarm` ... to manage a cluster (swarm)
  
  * `docker service` ... to manage replicated containers (services) in the swarm


### Creating a Docker Swarm Cluster Node


```sh
export DIGITALOCEAN_PRIVATE_NETWORKING=true
export DROPLETS_API="https://api.digitalocean.com/v2/droplets"
export BEARER_AUTH_TOKEN="Authorization: Bearer $DIGITAL_OCEAN_TOKEN"
export JSON_CONTENT="Content-Type: application/json"

```

- replace the fingerprint with your own 
```bash 

CONFIG='{"name":"swarm-manager","tags":["demo"],
	"size":"s-1vcpu-1gb", "image":"docker-20-04",
	"ssh_keys":["01:97:fe:0a:01:e3:a9:68:99:60:b5:e9:74:30:8f:71"]}'

SWARM_MANAGER_ID=$(curl -X POST "$DROPLETS_API" -d "$CONFIG"\
	-H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
	| jq -r .droplet.id ) && sleep 5 && echo $SWARM_MANAGER_ID
```

**Note:** Wait with below command till the droplet is active, unless there won't be an IP address
```bash

export JQFILTER='.droplets | .[] | select (.name == "swarm-manager") 
	| .networks.v4 | .[]| select (.type == "public") | .ip_address'


export SWARM_MANAGER_IP=$(curl -s GET "$DROPLETS_API"\
    -H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
    | jq -r "$JQFILTER") && echo "SWARM_MANAGER_IP=$SWARM_MANAGER_IP"

```

See: [Generating ssh key fingerprint](https://superuser.com/a/453022), [API doc for creating a droplet](https://docs.digitalocean.com/reference/api/api-reference/#operation/droplets_create) 


---

### Creating Worker Nodes


#### Worker1
```bash
WORKER1_ID=$(curl -X POST "$DROPLETS_API"\
       -d'{"name":"worker1","tags":["demo"],"region":"fra1",
       "size":"s-1vcpu-1gb","image":"docker-20-04",
       "ssh_keys":["a7:39:2c:a6:21:f8:a2:6d:33:a7:d9:87:1f:c9:d4:57"]}'\
       -H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
       | jq -r .droplet.id )\
       && sleep 3 && echo $WORKER1_ID
```
**Note:** Wait with below command till the droplet is active, unless there won't be an IP address
```bash

export JQFILTER='.droplets | .[] | select (.name == "worker1") | .networks.v4 | .[]| select (.type == "public") | .ip_address'


export WORKER1_IP=$(curl -s GET "$DROPLETS_API"\
    -H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
    | jq -r "$JQFILTER")\
    && echo "WORKER1_IP=$WORKER1_IP"

```



#### Worker2
```bash
WORKER2_ID=$(curl -X POST "$DROPLETS_API"\
       -d'{"name":"worker2","tags":["demo"],"region":"fra1",
       "size":"s-1vcpu-1gb","image":"docker-20-04",
       "ssh_keys":["a7:39:2c:a6:21:f8:a2:6d:33:a7:d9:87:1f:c9:d4:57"]}'\
       -H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
       | jq -r .droplet.id )\
       && sleep 3 && echo $WORKER2_ID
```
**Note:** Wait with below command till the droplet is active, unless there won't be an IP address
```bash

export JQFILTER='.droplets | .[] | select (.name == "worker2") | .networks.v4 | .[]| select (.type == "public") | .ip_address'


 export WORKER2_IP=$(curl -s GET "$DROPLETS_API"\
    -H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
    | jq -r "$JQFILTER")\
    && echo "WORKER2_IP=$WORKER2_IP"

```




### Making `swarm-manager` a Cluster Manager



##### Open the ports that Docker needs
```sh
ssh root@$SWARM_MANAGER_IP "ufw allow 22/tcp && ufw allow 2376/tcp &&\
ufw allow 2377/tcp && ufw allow 7946/tcp && ufw allow 7946/udp &&\
ufw allow 4789/udp && ufw reload && ufw --force  enable &&\
systemctl restart docker"
```
Read about the [roles of the ports](https://docs.docker.com/engine/swarm/swarm-tutorial/#the-ip-address-of-the-manager-machine)


##### Initialize the swarm
```sh
ssh root@$SWARM_MANAGER_IP "docker swarm init --advertise-addr $SWARM_MANAGER_IP"

```


```bash
Swarm initialized: current node (sozjy3nmfrieacm2pbgj41ek3) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-4rndqz4hwe38wtbl9fwgj33rk48ok3hri7a0xy42o7sf5ll38z-afkri2vu57m5z31v34bny16aj 142.93.109.102:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```



### Converting node-1 and node-2 to Workers

##### Let's get that token from the swarm-manager

```sh
$ ssh root@$SWARM_MANAGER_IP "docker swarm join-token worker -q"
SWMTKN-1-4rndqz4hwe38wtbl9fwgj33rk48ok3hri7a0xy42o7sf5ll38z-afkri2vu57m5z31v34bny16aj

$ WORKER_TOKEN=`ssh root@$SWARM_MANAGER_IP "docker swarm join-token worker -q"
```

##### and build a command that we can run on node-1 and node-2 to join the swarm.
```sh
REMOTE_JOIN_CMD="docker swarm join --token $WORKER_TOKEN $SWARM_MANAGER_IP:2377"

ssh root@$WORKER1_IP "$REMOTE_JOIN_CMD"
```

```
  This node joined a swarm as a worker.
```

```sh
ssh root@$WORKER2_IP "$REMOTE_JOIN_CMD"
```

```
  This node joined a swarm as a worker.
```




### Seeing the state of the cluster on the manager

```sh

$ ssh root@$SWARM_MANAGER_IP "docker node ls"

ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
sozjy3nmfrieacm2pbgj41ek3 *   node-0              Ready               Active              Leader              18.09.0
hy6ie5xq561f9w1zpiyaqkrk5     node-1              Ready               Active                                  18.09.0
```



### Starting a Service

Now that everything is setup, let's run a service on our cluster:

```sh
$ ssh root@$SWARM_MANAGER_IP "docker service create -p 8080:8080 --name appserver stifstof/crashserver"
overall progress: 0 out of 1 tasks
...
overall progress: 1 out of 1 tasks
verify: Waiting 5 seconds to verify that tasks are stable...
...
verify: Waiting 1 seconds to verify that tasks are stable...
verify: Service converged
```

... be patient about 1-2 min ..


### Checking the state of the service


```bash
$ ssh root@$SWARM_MANAGER_IP "docker service ls"
ID                  NAME                MODE                REPLICAS            IMAGE                        PORTS
ttkqm9wzthgu        appserver           replicated          1/1                 stifstof/crashserver:latest   *:8080->8080/tcp
```

You may directly ask for the state of a service with

```bash
$ ssh root@$SWARM_MANAGER_IP "docker service ps appserver"
```


Now, on a Mac you can: 

```sh
$ open http://$SWARM_MANAGER_IP:8080
```

Alternatively, navigate manually to the swarm manager's IP port 8080 and see the webpage served. 




### Checking that the Swarm also restarts services


To demonstrate this we used the ***crashserver service***: a webserver which kills itself three seconds after serving an http request

Take some time and observe the behavior of the container before continuing with the guide. 
- note how the infrastructure is self-healing, by checking the state of the service multiple times after an invocation as shown above.
- the service becomes unavailable while Swarm is recreating the container after it has been killed



### Scaling the service to increase availability?

```bash
$ ssh root@$SWARM_MANAGER_IP "docker service scale appserver=5"
$ ssh root@$SWARM_MANAGER_IP "docker service ls"

ID                  NAME                MODE                REPLICAS            IMAGE                        PORTS
ttkqm9wzthgu        appserver           replicated          5/5                 stifstof/crashserver:latest   *:8080->8080/tcp



$ ssh root@$SWARM_MANAGER_IP "docker service ps appserver"


ID                  NAME                IMAGE                        NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
vbg02o9bsaog        appserver.1         stifstof/crashserver:latest   node-1              Running             Running 7 minutes ago
mudpe1lokpj7        appserver.2         stifstof/crashserver:latest   node-0              Running             Running 13 seconds ago
t7enei6pz4jw        appserver.3         stifstof/crashserver:latest   node-0              Running             Running 12 seconds ago
sfpn4f2kg5nq        appserver.4         stifstof/crashserver:latest   node-1              Running             Running 39 seconds ago
wa8f99b6t199        appserver.5         stifstof/crashserver:latest   node-0              Running             Running 12 seconds ago
```



### Does the replication work?

You should now be able to invoke the webpage without seeing the error-page each time the container is killed, but instead see the request being served by another container. Nice!

Although it is possible to kill all container by manically invoking the /status endpoint, if you want to test the self-healing feature of swarm, you can invoke the /kill endpoint, which will kill the container immediately, so you don't have to wait.  



### Checking that the routing mesh works as advertised


```sh
open http://$WORKER1_IP:8080
```

```sh
open http://$WORKER2_IP:8080
```

Note: Make sure to open port 8080 from the firewall.



### Cleaning up to not pay anymore...



```bash
curl -X DELETE\
  -H "$BEARER_AUTH_TOKEN" -H "$JSON_CONTENT"\
  "https://api.digitalocean.com/v2/droplets?tag_name=demo"
  
```
See: [documentation](https://docs.digitalocean.com/reference/api/api-reference/#operation/droplets_destroy_byTag)  for the delete API endpoint


Note:
- The interactive guide is based on the [tutorial at DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-a-cluster-of-docker-containers-with-docker-swarm-and-digitalocean-on-ubuntu-16)

### Next step: declarative deployment with `docker stack`

In this exercise you used imperative commands (`docker service create`, `docker service scale`). For your projects, you'll want the declarative approach: add a `deploy` key to your existing `docker-compose.yml` and use `docker stack deploy`. See the [lecture slides](./Slides.md#how-to-migrate-from-docker-compose-to-docker-swarm) for details.









	
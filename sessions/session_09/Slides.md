# Availability

![](assets/if-coding-is-solved.png)

Mircea Lungu, Associate Professor,<br>
[IT University of Copenhagen, Denmark](https://www.itu.dk)<br>
`mlun@itu.dk`

# Introduction

## An anticipated launch

The dream of Obama was to offer affordable healthcare insurance to all US citizens. Highly anticipated, the launch of [healthcare.gov](https://www.cbsnews.com/news/healthcaregov-plagued-by-crashes-on-1st-day/) was a disaster: it resulted in the system experiencing a quick performance degradation to the point where the whole website was down soon after its official launch. 

![360](images/healthcare_gov.png)


> "I was excited to get on, and I can't, so yeah I'm disappointed," Matt Warren said.
> Matt Warren said he will try again Wednesday. There are about six million uninsured residents in Texas. It's estimated half of them could be covered by the Affordable Care Act.
https://www.cbsnews.com/news/healthcaregov-plagued-by-crashes-on-1st-day/

The reason? Too many users wanted to use it at the same time!

How do we technically describe what happened? We say that 

> the system had low **availability** 
> 
It failed to serve users due to insufficient **scalability** under load.

### Lack of scalability is often the reason for lack of availability 

#### Ticketmaster down for Taylor Swift concert

- Ticketmaster being [down](https://www.educative.io/blog/taylor-swift-ticketmaster-meltdown) when 13million fans showed up to buy tickets instead of the expected 1.5million

#### Twitter became famous for their "*fail whale*"
- Twitter used to [show the fail whale a lot](https://medium.com/@yadavmpadiyar/scaling-up-1-twitter-from-fail-whale-to-real-time-global-scale-d4af68965a70) because of their Rails monolithic architecture was hard to scale. Went from 200-300 req/s per host (Ruby) to 10,000-20,000 (Java/Scala)

### Lack of availability can also be due to misconfiguration or human error

- A [BGP misconfiguration](https://blog.cloudflare.com/october-2021-facebook-outage/) took down Facebook, Instagram, and WhatsApp for 6 hours. Engineers couldn't even enter buildings because ID systems were down too
- A GitLab engineer accidentally [ran `rm -rf` on the production database](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/) during a maintenance operation. 5 out of 5 backup methods failed. They lost 6 hours of data

## Availability  and how to strive for it

### What is availability? 

**Availability** is 
- a quality attribute... 
- that is expressed as the **proportion of time that a system or service is operational** and accessible for use. 

High availability means that users can access the system without significant interruptions or downtime.

![](assets/gh-platform-uptime.png)

Source: https://x.com/ThePrimeagen/status/2036567606711251184

### We measure availability with the *number of nines uptime* metric

We measure with the "number of nines" metric. e.g., an uptime of 99.9% is called "three nines", and it means that in a given period, the system was up for 99.9% of the time. 

Every additional "nine" increases the expectations on your system uptime. 

![](assets/number-of-nines.png)

**Relevant** in the context of 
- mission-critical systems
- healthcare
- banks
- cloud APIs 
- online services and apps


### How do systems fail to achieve availability? 


#### 1. When Individual Components Fail


This is probably the architecture that many of your systems have at the moment. 

We say that such an architecture has a **single point of failure**. 

This can be defined as an architecture in which ***a part of the system failing will stop the entire system from working***. 

![](images/possible_arch1.png)

If Node 1 is down, then our whole system is down!

---


#### 2. When Individual Components Are Overwhelmed

Personal story: demoing Zeeguu to a roomful of polyglots.


Scenario: 
> > Your user authentication system is slow, and your application becomes really popular with many users trying to create accounts at the same time. **The server’s CPU becomes a bottleneck** hashing algorithms used by the application is computationally intensive, causing login delays, and users going away from the system. 


We say that such an architecture has encountered a **congestion**, which is **reduced quality of service that occurs when a network node or link is attempting to handle more data than it can**. 

Possible Reasons for congestion 
- Seasonal spikes in demand
	- Highly anticipated launches (healthcare.gov)
	- Traffic surges (e.g. [The Slashdot effect](https://en.wikipedia.org/wiki/Slashdot_effect), etc.)
- Lack of monitoring and anticipating demand growth



### How to increase availability

#### 1. Eliminating Single Points of Failure

In system design **redundancy** means *adding extra components to the system in such a way that **if one component fails, another can take over**. 

Redundancy in system design is the solution to the single point of failure problem.


##### Cost and synchronization are the two tradeoffs that come with the increased availability of redundancy
- **Cost** -- it is more expensive to duplicate nodes
- **Synchronization** -- keeping redundant components in sync can be challenging -- see your distributed systems course and the CAP theorem (consistency, availability, partition: you can only have two)


##### Where did we get the inspiration from? 

We can learn from one of the most marvelous systems that we are aware of: the human body. 

It is resilient at multiple levels of abstraction. We have two lungs, two kidneys, two eyes, etc. 

![400](images/lung_redundancy.png)

And the ultimate replication: the DNA! Every cell has the whole DNA of the whole thing inside it! 


The solution nature found with respect to availability and removing single points of failure is: **redundancy.**

*Note: CS is always learning from biology. OO programming. Ant colony optimization. etc.*


#### 2. Designing Systems to Prevent Congestion

There are two main solutions to preventing congestion:

##### 1. **Performance optimization:** Ensuring that the system is designed and tuned to handle the expected load efficiently, reducing the risk of bottlenecks and failures.

E.g. 
- DB Indexes 
- Optimal data structures and algorithms

##### 2. **Scaling** -- when performance optimization is not enough

No matter how performant our algorithms, comes a time when we need a more powerful machine. There are two main approaches to scaling: 

1. **Vertical** -- getting a bigger machine
2. **Horizontal** -- creating a computational structure from multiple machines

# Vertical Scaling

## Vertical scaling literally means **replacing resources with larger or more powerful ones**

There are two ways to do it: 
* In a **physical server**: open the hood, and add: more memory, disk, etc. In a data center, replace a physical server with a more powerful one
* In a **VM**: reconfigure the machine programmatically


## When doing it for VMs there are many alternatives 
### Example 1. Vertical Scaling with the VirtualBox  GUI

1. **Power Off VM** 
2. Modify RAM and storage (either via GUI or CLI)
3. **Power On VM**
4. From within the VM update the OS wrt your new disk size (takes a while!)

![400](images/vertical-scaling-ui.png)

Repartitioning 
  - e.g. with `gparted` or similar tools

---

### Example 2: Vertical Scaling VirtuaBox from the CLI

```bash
$ VBoxManage list vms
"coursevm" {e072b310-1922-4113-93f5-2ca865e01722}
"lsd2018vm" {67fda2ea-7c3e-42f6-9a13-d0908020322d}
```

```bash
$ VBoxManage modifyvm "coursevm" --cpus 8
$ VBoxManage modifyvm "coursevm" --memory 8192
```


```bash
$ VBoxManage list hdds

UUID:           9953ea1b-7295-4547-94fa-209f49c258f5
Parent UUID:    base
State:          created
Type:           normal (base)
Location:       /path/to/node1ubuntu-16.04-amd64-disk001.vmdk
Storage format: VMDK
Capacity:       40960 MBytes
Encryption:     disabled
```

```sh
$ VBoxManage clonehd "9953ea1b-7295-4547-94fa-..." "cloned.vdi" --format vdi
$ VBoxManage modifymedium disk "cloned.vdi" --resize 65536
```

Notes:

Optionally, you may want to convert the disk back to `vmdk` with `VBoxManage clonehd "cloned.vdi" "resized.vmdk" --format vmdk`


See More:
      * Modification of RAM https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvm 
      * Modification of storage https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvd

---

### Example 3: Vertical Scaling with DigitalOcean

Similar to VirtualBox, only that on the Web

**You can only resize VMs that are not running**.

![](images/DO-resize-options.png)
    


See https://www.digitalocean.com/docs/droplets/how-to/resize/#resizing-via-the-control-panel

---

### Example 4: Vertical Scaling With the REST API  of DigitalOcean

```bash
$ curl -X POST -H 'Content-Type: application/json' \
	   -H "Authorization: Bearer $DIGITAL_OCEAN_TOKEN" \
	   -d '{"type":"resize","size":"s-2vcpu-4gb"}' \
	   "https://api.digitalocean.com/v2/droplets/$DROPLET_ID/actions" | jq
```

*Notes:* 
- $DIGITAL_OCEAN_TOKEN environment variable is defined
- $DROPLET_ID is defined
- Image types and sizes at: https://slugs.do-api.dev/
--

- Resize CPU and RAM **automatically shuts down the droplet** 

```bash
$ curl -X POST -H 'Content-Type: application/json' \
-H "Authorization: Bearer $DIGITAL_OCEAN_TOKEN" \
-d '{"type":"power_on"}' \
"https://api.digitalocean.com/v2/droplets/$DROPLET_ID/actions"
```

Discussion: why REST is particularly nice for IaC

---

## Vertical scaling is appropriate for legacy systems, specific software, and predictable workload

- Legacy systems (e.g. bank mainframes)

- Some types of software that does not scale well horizontally. e.g. databases that don't cluster well

- Predictable growth -- when you can anticipate the growth of demand on your system, and that growth can be serviced by the vertically scaled infra



## Vertical scaling might not be ideal for high variability workloads, and might not be possible for some really large workloads

- You have to adapt fast to varying workload (e.g. Black Friday for web shops, Ticketmaster when Taylor Swift concerts, etc.). 

- When you also have to scale down; often more complicated than upscaling

- When you can't afford downtime - it implies switching machines off and on (physical but also VM!)

- Some workloads are simply too big for vertical scaling
	- Facebook, **Google**, etc. 
	- Scientific computing
		- seismic analysis 
		- biotechnology
		- SETI@Home



# Horizontal Scaling

= Preventing congestion by **increasing the number of computing nodes**.

Two components:
1. **adding more machines to a setup** and
2. **making all the machines share the responsibilities**

![420](images/scaling-graphic.png)

![](assets/Pasted%20image%2020260327131351.png)
## From bigger machines to more machines

- [As of **2000** Google can not host all their DB on a single machine](https://www.linkedin.com/pulse/how-did-google-scale-untold-story-shrey-batra/?trk=articles_directory).
	- The only way they can keep up is buying normal computers and wiring them together into a fleet
	- Because half the cost of these computers is considered junk—floppy drives, metal chassis—the company orders raw motherboards and hard drives and *sandwich* them together
- In **2004** they introduce the [MapReduce paper](papers/mapreduce-osdi04.pdf) to propose an architecture for distributing the DB and subsequent queries over an array of machines

*We take this for granted today, but it was a very revolutionary idea two decades ago*

Distributing data and computation across machines solves the congestion problem. But it doesn't solve the single point of failure problem. For that, we need **replication**.

## Replicating Services

Load Balancing = **Distributing traffic to — and computation across — multiple replicated servers**

- Ensures no single server bears too much demand
- Improves responsiveness
- Adds redundancy: if one replica goes down, others can take over

![](images/load_balancing.png)

Solves **scaling** and SPF at the application server level but...

... load balancer is still SPF ^^!

Image from: [Horizontally Scaling PHP Applications](https://blog.digitalocean.com/horizontally-scaling-php-applications/)


---
### Redundant Load Balancer Setup

How to make the balancer not anymore a single point of failure: [Heartbeat and Floating IP](https://www.digitalocean.com/community/tutorials/how-to-create-a-high-availability-setup-with-heartbeat-and-floating-ips-on-ubuntu-16-04))

[![600](images/ha-diagram-animated.gif)](https://assets.digitalocean.com/articles/high_availability/ha-diagram-animated.gif)

- [Floating IP](https://blog.digitalocean.com/floating-ips-start-architecting-your-applications-for-high-availability/)  (Reserved IP since 2022)
	 - DigitalOcean name for static IPs
	 - Equivalents on other platforms, e.g. Elastic IPs @ Amazon
- Keepalived - daemon used for health check



Where to read more about this setup
- [Load Balancing as a Service on DO](https://blog.digitalocean.com/load-balancers-simplifying-high-availability/)
- [HAProxy with Keepalived on Ubuntu](https://kifarunix.com/configure-highly-available-haproxy-with-keepalived-on-ubuntu-20-04)

---

### Limitations of load balancing

Load balancing and replication solve traffic distribution and SPF, but they don't manage the fleet. As the number of nodes grows, who...
- ... spins up new services when one crashes?
- ... decides which node runs which service?
- ... handles rolling out updates without downtime?
- ... scales up or down based on demand?

That's what **container orchestration** adds on top of load balancing.

## Container Orchestration Platforms

Container orchestration tools...
1. ... **manage computing nodes** and **services**
2. ... **schedule tasks** in a resource aware manner


### Popular Alternatives

![400](images/tools_that_help_scaling.png)

#### **Docker Swarm Mode**
- Comes with Docker by default
- The easiest to use from all the alternatives
- Development has slowed, but it's [not deprecated](https://www.mirantis.com/blog/swarm-is-here-to-stay-and-keeps-getting-better-in-security-and-ease-of-operations/) and is supported through at least 2030
- We use it in this course because it's the simplest way to learn orchestration concepts

#### **Kubernetes**
  * Originally developed at Google
  * The industry standard — [82% of container users run it in production](https://thedecipherist.com/articles/docker_swarm_vs_kubernetes/)
  * Much more powerful, but significantly more complex ([see hacker news discussion](https://news.ycombinator.com/item?id=26271470))

Others: OpenShift (Red Hat's enterprise Kubernetes), Nomad (HashiCorp), and [many more](https://devopscube.com/docker-container-clustering-tools/)

  

### Docker Swarm Mode

#### Main Concepts

The following [concepts are essential for understanding Docker Swarm mode](https://docs.docker.com/engine/swarm/key-concepts/#what-is-a-swarm)

1. **Swarm** / **Cluster** = a group of nodes that work together to create a distributed system
2. **Node** = A (virtual) machine participating in a swarm
	  - **Managers**
	  - **Workers**
3. **Service** = a replicated process
4. **Task** = an instance of a process
5. **Routing Mesh** = network overlay mechanism

These concepts have equivalents in other orchestration environments — the names will differ (e.g. Kubernetes calls services "Deployments," tasks "Pods") and there will be many more concepts, but the core ideas are the same.


#### 1. Manager Node

  * Maintain swarm (cluster) state
  * Schedule services on the nodes
  * Designed for redundancy: *n manager swarm* tolerates loss of *(n-1)/2* managers


![600](images/swarm_diagram.png)

Notes: 
- Docker recommends a *maximum of seven manager nodes for a swarm* (!?!)
- More managers does NOT mean increased scalability or higher performance. In general, the opposite is true


#### 2. Worker Node

A machine which from the POV of the swarm
  * executes Docker containers
  * has at least one manager node

Notes: 
  * By default, all managers are also workers


See more [https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes/](https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes/)

#### 3. Service

- The primary abstraction of user interaction with the swarm 
- Defined by: 
	- docker image
	- the **port** where the service is available outside of the swarm
	- number of replicas to run in the swarm


![400](images/service-task-container.png)

 More on [services](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/)

#### Types of Services

Can be 
- **replicated** - allows you to select the level of replication 
- **global** - exactly one replica running on each node

To think about:
- *What service does it make sense to have "global" replication for?*
- *What services should not be replicated (i.e., replication level = 1)?*

  
![500](images/replicated_vs_global.png)


Good examples of global service? A **log shipper** or a **monitoring container**. It is important to ensure that the service is running on every node. By deploying the service as a global service, you can ensure that every node in the cluster has a copy of the service running, which can collect data from that node and forward it to a centralized location.


#### 4. Task

- The atomic scheduling unit of swarm
- Carries **a container and the commands to run inside it**
- Manager nodes assign tasks to worker nodes according to the number of replicas set in the service scale

*"A service is a description of a desired state, **and a task does the work**"*


#### 5. The Routing Mesh

- Routes all incoming requests to published ports on available nodes to an active container

- Enables each node in the swarm to accept connections 
  - on published ports 
  - for any service running in the swarm
  - even if there’s no task (container) running on the node

- Supports load balancing in Docker Swarm


Read more:  https://docs.docker.com/engine/swarm/ingress

## Stateless vs. Stateful Services 

There are two types of services

- **Stateless**
	- Does not maintain any internal state or data between requests. 
	- Each request is handled independently
	- Ideal for horizontal scaling and load balancing.

- **Stateful** 
	- Maintains internal state or data that persists across requests or instances
	- Examples include databases and file storage services 
	- Replicating stateful services introduces challenges related to data consistency, synchronization, and failover

Note that **most of the orchestration platforms** are **optimized** for you to have **stateless services** because they can be replicated easily.

### Making your services stateless

General principle: **a container should be disposable**. If you can kill it and spin up a new one without the user noticing, your state management is correct.


#### Handling user sessions across replicas

**The session problem**: If a user authenticates on one replica and their next request is routed to a different replica, their session is lost. The second replica has no idea they're logged in. This is the most common reason stateful services break under replication.

Common approaches to solving this:

1. **Stateless tokens (JWT)** — encode session data in the token itself. No server-side state needed. Signing key, is a config value shared across replicas. Simplest if your session data is small (user ID, role, expiry).
2. **External session store** — move sessions to Redis, Memcached (in-memory key-value stores — fast because everything lives in RAM, fine for sessions since losing them just means users re-login), or the database. Any replica can look up the session.
3. For load balancing: **Sticky sessions** — the load balancer always routes the same user to the same replica. Works but if that replica dies, the session is lost.


#### Specifically for your project: Handling the Latest ID

You very likely have to take the Latest ID out of the container too — otherwise every container sees a different value.

Solutions:
1. **Database** — simplest, you already have one. A single read/write won't be a bottleneck.
2. **Redis** — faster in some cases, unlikely for a single int. Also adds a dependency you might not otherwise need.

If you go with JWT for auth + database for Latest ID, you don't need Redis at all. That's the simplest path.

## Tradeoffs of horizontal scaling

**It can be more complicated than vertical** (see [hacker news thread on k8s](https://news.ycombinator.com/item?id=26271470))

**Because Google and Facebook need it**... 
- ... that's why probably you don't 
- ... some of these technologies can be quite complicated (e.g. k8s -- aims to be a **generalized solution** to distributed systems design that ... also works at Google! )




# Upgrading replicated services

Two possible upgrade strategies: 

1. Blue-Green
2. Rolling Updates


#### Blue-green

Conceptually: 
- **Two identical environments, where only one (green) is hot at any time**
- Use the blue environment as your staging environment for the final testing step for your next deployment

![300](images/blue-green-fowler.png)

Step by step: 
  1. Currently deployed application (Green) is serving incoming traffic
  2. New version (Blue) is deployed and tested, but not yet receiving traffic
  3. When Blue is ready, orchestration / load balancer starts sending incoming traffic to it too
  4. For a while: two versions of the application run in parallel
  5. Orchestration / load balancer stops sending incoming traffic to the "Green"; "Blue" is handling all the incoming traffic
  6. Green can now be safely removed
  7. Blue is marked as Green...

More about [colorful deployments](https://opensource.com/article/17/5/colorful-deployments) 




#### Rolling Updates

**Deploy the upgrade in rolling iterations**

Rolling Updates in Docker Swarm:
1. Stop the first *task*
2. Schedule update for the stopped task
3. Start the container for the updated task
4. If the update to a task returns RUNNING, wait for the specified delay period (`--update-delay` flag) then start the next task
5. If, at any time during the update, a task returns FAILED, pause the update
  ![250](images/rolling.gif)
Note: 
- **You need at least two replicas otherwise there will be downtime**
- [Rolling Updates Swarm Tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/ ) 


### Upgrade strategies in docker swarm 

Two `update-order` options: (stop-first|start-first) 
- `stop-first` (default) -- corresponds to rolling updates
- `start-first` -- corresponds to blue-green service deployment





# Practicals

## How to migrate from `docker-compose.yml` to docker swarm?

It's simple. 

You **add a little bit of extra information** in the `docker-compose.yml` under the **deploy** key:
- replicas
- [placement constraints](https://docs.docker.com/engine/swarm/services/): labels, roles, other props of nodes
- update strategies, restart strategies
- [etc](https://docs.docker.com/compose/compose-file/deploy/).

Example:
```
  api:
    image: itudevops/go-minitwit-api:TAG
    deploy:
      replicas: 2
      update_config:
        delay: 10s
        order: start-first
      placement:
        constraints:
          - "node.role==manager"
          - "node.hostname!=dbvm"
          - "node.label==frankfurt"
```

## `docker stack` — deploying a compose file to a swarm

Instead of `docker compose up`, in a swarm you use `docker stack`:

```bash
$ docker stack deploy -c docker-compose.yml myapp
```

Key differences from `docker compose`:
- `docker stack` **ignores** `build:` directives — images must already be built and pushed to a registry
- `docker stack` **reads** the `deploy:` key — `docker compose` ignores it
- Stacks are managed as a unit: `docker stack ls`, `docker stack services myapp`, `docker stack rm myapp`

See: [The Difference Between Docker Compose And Docker Stack](https://vsupalov.com/difference-docker-compose-and-docker-stack/)



# Scaling in practice: you can go quite far without orchestration

- [Brief History of Scaling at LinkedIn](https://engineering.linkedin.com/architecture/brief-history-scaling-linkedin): *"An easy fix we did was classic vertical scaling ... While that bought some time, we needed to scale further"*. Started vertical, had to go horizontal. 
- Thibault Duplessis on the architecture of Lichess — no orchestration, still works.
- StackOverflow does not use horizontal scaling ([podcast](https://hanselminutes.com/847/engineering-stack-overflow-with-roberta-arcoverde), [tweet](images/StackOverflowInfraTweet.png)). Still works.

![400](images/StackOverflowInfraTweet.png)

# What Next?

Exercise: [**Swarm creation on DigitalOcean**](./README_EXERCISE.md).
Practical: [**Scale your API**](README_TASKS.md) in preparation for the **future increase in user requests** ^^!!

# References
- [Redundancy in Distributed Systems](https://csis.pace.edu/~marchese/CS865/Lectures/Chap8/New8/Chapter8.html) — Tanenbaum's elaborate treatment of redundancy and fault tolerance


# History

2025, added docker stack discussion
2026, added availability stories (Ticketmaster, Twitter, Facebook, GitLab), stateless services section, limitations of load balancing bridge
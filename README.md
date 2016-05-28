# About this Repo

This is the Git repo of the Docker [official image](https://docs.docker.com/docker-hub/official_repos/) for [n42ce_master](https://hub.docker.com/r/n42inc/n42ce_master/). See [the Docker Hub page](https://hub.docker.com/r/n42inc/n42ce_master/) for the full readme on how to use this Docker image and for information regarding contributing and issues.

Reside on swarm master , listen swarm events and send to redis.[n42ce_slave](https://hub.docker.com/r/n42inc/n42ce_slave/) reside on swarm slave node's and listen events from redis.


Docker deployment monitoring for applications, collects data to provide application topology discovery, multilayer diagnostic views and application sub components performance analytics

## Method 1:
Send a mail to <b>info@networks42.com</b> to obtain the key

wget -O n42inc_communityedition.sh https://raw.githubusercontent.com/N42Inc/docker-compose/master/n42inc_communityedition.sh && sudo bash n42inc_communityedition.sh <key>

Replace key with the userkey provided by N42.

Requirements:
      1.docker compose
      2.python
      
Ports used for communication with monitoring server :
```
   redis: Port:6379  IP: 52.73.171.150   
```
4.Log into [http://54.67.112.100:8080/](http://54.67.112.100:8080/)  with provided crediantials.

import sys
import docker
import os,redis,re,sys
import subprocess
import json
swarmmaster_ip = "127.0.0.1:4000"#os.environ['swarmmaster_ip']
config = {
    'host': '52.73.171.150',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)
def send(channel,message):
        print 'Sendind Notification to the channel ------> "{channel}"'.format(**locals())
        r.publish(channel, message)

# start listening for new events
def docker_events():
        base_url = "tcp://"+swarmmaster_ip
        cli = docker.Client(base_url)
        events = cli.events(decode=True)
        for event in events:
           listen_events = ["start","stop"]
           if event['Action'] in listen_events:
                        #print event
                        action = event['Action']
                        cid = event['id'][:12]
                        cname = event['Actor']['Attributes']['name']
                        node_ip = event['node']['Ip']
                        node_name = event['node']['Name']
                        #swarm_id = event['Actor']['Attributes']['com.docker.swarm.id']
                        image = event['Actor']['Attributes']['image']
                        event_dict = {"action":action,"cid":cid,"cname":cname,"node_ip":node_ip,"node_name":node_name,"image":image}
                        key = os.environ['key'] + "-info"
                        print "key:"+key
                        print "event_dict:",event_dict
                        send(key,event_dict)

docker_events()



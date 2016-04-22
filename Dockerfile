FROM ubuntu:latest
MAINTAINER Networks42
RUN apt-get update && apt-get install -y supervisor python2.7 conntrack python-pip bridge-utils vim
RUN apt-get install -y vim
RUN pip install potsdb redis docker-py
COPY swarmevents.py /root/swarmevents.py
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

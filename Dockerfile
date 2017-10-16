FROM ubuntu:16.04
MAINTAINER Svetlana Zlobina <svetlanazlobina97@gmail.com>

RUN apt-get -y update
RUN apt-get -y install python3.6

ENV WORK /usr/local/bin
ADD . $WORK/python3.6

WORKDIR $WORK/python3.6

RUN mkdir -p /var/www/html

EXPOSE 80

CMD python httpd.py
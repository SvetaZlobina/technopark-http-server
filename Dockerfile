FROM ubuntu:16.04
MAINTAINER Svetlana Zlobina <svetlanazlobina97@gmail.com>

RUN apt-get -y update
RUN apt-get -y install python
RUN pip install --upgrade -y pip enum34

ENV WORK /usr/local/bin
ADD . $WORK/python2.7

WORKDIR $WORK/python2.7

RUN mkdir -p /var/www/html

EXPOSE 80

CMD python httpd.py
FROM ubuntu:16.04
MAINTAINER Svetlana Zlobina <svetlanazlobina97@gmail.com>

ENV WORK /opt
ADD . $WORK/httpd

WORKDIR $WORK/httpd

RUN mkdir -p /var/www/html

EXPOSE 80

CMD python httpd.py
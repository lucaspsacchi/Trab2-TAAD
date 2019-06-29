FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt-get install python2.7

CMD [ "python", "./server.py" ]

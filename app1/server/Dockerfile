FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt install python-pip

CMD [ "python", "./server.py" ]

FROM ubuntu

COPY . /server

WORKDIR /server

EXPOSE 6000/udp

RUN apt-get update && apt-get install -y \
    python-pip

CMD [ "python", "./server.py" ]

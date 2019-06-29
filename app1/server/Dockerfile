FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt-get update && apt-get install -y \
    python-pip

CMD [ "python", "./server.py" ]

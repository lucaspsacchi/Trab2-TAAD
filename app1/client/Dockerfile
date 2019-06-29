FROM ubuntu

COPY . /client

WORKDIR /client

RUN apt-get update && apt-get install -y \
    python-pip

CMD [ "python", "./client.py" ]

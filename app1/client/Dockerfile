FROM ubuntu

COPY . /client

WORKDIR /client

RUN apt-get update && apt-get install -y

CMD [ "python", "./client.py" ]

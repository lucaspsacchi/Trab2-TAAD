FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt-get update && apt-get install -y

CMD [ "python", "./server.py" ]

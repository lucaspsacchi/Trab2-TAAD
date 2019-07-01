FROM python:3.7-alpine

WORKDIR /tmp
COPY deps.txt deps.txt
RUN pip install -r deps.txt

ADD . .
WORKDIR .

CMD ["python3.7", "./client.py"]
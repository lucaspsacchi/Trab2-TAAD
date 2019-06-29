#!/usr/bin/env python
# -*- coding: utf-8 -*-

#serv_sock.py
import socket

HOST = 'localhost'
PORT = 50000

def server():

  # Cria socket UDP
  sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
  sock.bind((HOST, PORT))

  while True:
    # print("Esperando envio...")

    # Recebe o nome do arquivo que está enviando
    nome, addr = sock.recvfrom(1024)
    arq = open('server/' + nome, 'w')

    while True:
      # Define o tamanho máximo da mensagem
      info, addr = sock.recvfrom(1024) # Tamanho do buffer é de 1024 bytes
      # while info[-1:] == '\0':
      #     info = info[:-1]
      if info == "close":
        break
      # Decodifica a mensagem em ...
      var = info.decode('utf-8')
      # print('Type:' + str(type(var)) + '\nvar: ' +  var)
      arq.write(var)

    arq.close()
server()

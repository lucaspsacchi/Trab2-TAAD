#!/usr/bin/env python
# -*- coding: utf-8 -*-

#client_sock.py
import socket
import os

HOST = 'localhost' #coloca o host do servidor
PORT = 50000

def client():

    # Cria o socket UDP
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

    while True:
      print("Escolha um dos 3 arquivos:")
      print("0 - sair")
      print("1 - exemplo1.txt")
      print("2 - exemplo2.txt")
      print("3 - exemplo3.txt")
      aux = input()

      if (aux == 1):
        nome = "exemplo1.txt"
      elif (aux == 2):
        nome = "exemplo2.txt"
      else:
        nome = "exemplo3.txt"

      # Sai da aplicação
      if aux == 0:
        break

      # Abre o arquivo para leitura
      arq = open(nome, 'rb')

      # Envia o nome do arquivo
      sock.sendto(nome, (HOST, PORT))

      # Envia a mensagem pelo socket para um ip e uma porta destino
      for info in arq.readlines():
        print(str(info))
        sock.sendto(info, (HOST, PORT))

      # Fechando o arquivo
      info = "close"
      sock.sendto(info, (HOST, PORT))

      arq.close()

    sock.close()

client()

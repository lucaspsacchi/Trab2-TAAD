#client_sock.py
import socket

HOST = 'localhost' #coloca o host do servidor
PORT = 50000

def client():

    # Cria o socket UDP
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

    arq = open('c:/UFSCAR/7º Semestre/Top Fábio/Trab2-ClientServer/exemplo.txt', 'rb')

    # Envia a mensagem pelo socket para um ip e uma porta destino
    for info in arq.readlines():
        print(str(info))
        sock.sendto(info, (HOST, PORT))
    
    arq.close()
    sock.close()

client()
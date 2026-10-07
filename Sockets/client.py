"""
CLIENT

socket -> connect -> send -> recv -> close


"""

import socket
import threading


def enviarMsg(c):
    while True:
        message = str(input("Mensagem a ser enviada: "))
        if message.lower() == "sair": 
            c.shutdown()
            break
        c.sendall(message.encode()) 

def receberMsg(c):
    while True:
        data = c.recv(1024)
        if not data: break
        print('Recebido: ', data.decode())


def iniciarClient():
    client_socket = socket.socket(socket.AddressFamily.AF_INET, socket.SocketKind.SOCK_STREAM)

    host = '127.0.0.1'
    port = 2203

    with client_socket as c:
        c.connect((host, port))

        with c:
            c.sendall(b'Hello World from Socket Client')
            envioMsgThread = threading.Thread(target=enviarMsg, args=[c])
            recebimentoMsgThread = threading.Thread(target=receberMsg, args=[c])
            envioMsgThread.start()
            recebimentoMsgThread.start()
            envioMsgThread.join()
            recebimentoMsgThread.join()
        print("encerrando conexão..")
        c.close()

if __name__ == "__main__":
    iniciarClient()
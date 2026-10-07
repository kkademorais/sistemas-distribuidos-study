"""
CLIENT

socket -> connect -> send -> recv -> close


"""

import socket

client_socket = socket.socket(socket.AddressFamily.AF_INET, socket.SocketKind.SOCK_STREAM)

host = '127.0.0.1'
port = 2203

with client_socket as c:
    c.connect((host, port))

    with c:
        c.sendall(b'Hello World from Socket')
        while True:
            message = str(input("Mensagem a ser enviada: "))
            if message.lower() == "sair": break
            c.sendall(message.encode())
            data = c.recv(1024)
            print('Recebido: ', data.decode())
        print("encerrando conexão..")
        c.close()
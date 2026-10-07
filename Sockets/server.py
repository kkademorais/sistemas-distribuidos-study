"""
SERVER:

socket -> bind -> listen -> accept -> recv -> send -> recv -> close

"""


import socket

    # socket: cria objeto socket em ipv4 e usando tcp
server_socket = socket.socket(socket.AddressFamily.AF_INET, socket.SocketKind.SOCK_STREAM)

host = '127.0.0.1' # localhost
port = 2203

with server_socket as s:

        # bind: associa o socket aos dois lados da comunicação
    s.bind((host, port))    

        # listen: server pronto pra receber conexões
    s.listen()

        # accept: socket aceita uma conexão
            # conn = objeto socket usado pra mandar e receber mensagem no canal
            # addr = endereço do outro lado conectado ao socket
    conn, addr = s.accept()

    print("Servidor aceitando conexões")
    with conn:
        print('Conectado ao endereço: ', addr)
        while True:
                # recv: recebe um buffer de X bytes
            data = conn.recv(1024)
            if data: print('Dado recebido: ', data)
            if not data: break  # se não receber = disconectar
            conn.sendall(data)
        conn.close()
    s.close()
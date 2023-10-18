#!/usr/bin/python3

import socket

server_socket=socket.socket(
socket.AF_INET, socket.SOCK_STREAM
)

host =socket.gethostname()
port = 444

server_socket.bind((host, port))

server_socket.listen(3)

while True:
    print("received connection from %s" %str(address))
    clients_socket, address = server_socket.accept()
    

    message = "Hello! Thanks for connecting" + "\r\n"

    clients_socket.send(message.encode('ascii'))

    clients_socket.close()
#!/usr/bin/python3

import socket

def banner(ip, port):
    sckt = socket.socket()
    sckt.connect((ip, int(port)))
    print(sckt.recv(1024))

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()
#!/usr/bin/python3

import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.settimeout(5)

host = input("Give me an IP to scan his ports: ")
port = input("Give me a port to scan: ")

def portScanner(port):
    try:
        if sckt.connect_ex((host, int(port))):  # Use int() to convert the input string to an integer
            print("The Port is Closed")
        else:
            print("The Port is Open")
        sckt.close()
    except Exception as e:
        print(f"An error occurred: {e}")

portScanner(port)
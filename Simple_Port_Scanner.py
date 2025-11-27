# This simple port scanner is for educational purposes only. The person who wrote the code does not accept any liability in any case.

import socket

ip = input("Write Ip adress: ")
port = int(input("Write port: "))

s = socket.socket()
s.settimeout(1)
try:
    s.connect((ip,port))
    print("Port is open.")
except:
    print("Port close.")
s.close()

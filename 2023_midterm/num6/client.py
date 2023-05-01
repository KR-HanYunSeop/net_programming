from socket import *

port = 7777
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)

while True:
    msg = input('Enter ping: ')
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
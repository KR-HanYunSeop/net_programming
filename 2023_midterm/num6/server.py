from socket import *

port = 7777
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode()
    print(data)
    
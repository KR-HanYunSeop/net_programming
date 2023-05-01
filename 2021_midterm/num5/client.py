from socket import *

addr = ('localhost',6666)
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(addr)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
    print(msg)
    sock.send(msg.encode())
    if(msg=='quit'):
        break
    data = sock.recv(BUFFSIZE)
    print('<- ',data.decode())
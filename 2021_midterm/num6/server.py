import socket
import random
port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 4:
        continue
    print('Received: ', msg.decode())

    sock.sendto(msg, addr)
    
    # sock.sendto('ack'.encode(), addr)
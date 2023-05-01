from socket import *
import random

BUFF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('',port))


while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
    s_sock.sendto(msg.encode(), addr)
    if random.randint(1, 10) <= 1:
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(data.decode(),addr))

    s_sock.sendto('ack'.encode(), addr)
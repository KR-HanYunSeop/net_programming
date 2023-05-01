from socket import *
import time

BUFF_SIZE = 1024
port = 5555
c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('', port))
while True:
    time_cnt = 0.1
    cnt = 0
    data = input('Enter a message: ')
    if data == 'q':
        break
    while True:
        c_sock.sendto(data.encode(), ('', port))
        cnt += 1
        c_sock.settimeout(time_cnt)

        if cnt == 4:
            break
        # print('Packet: Waiting up to {} secs for ack'.format(time))
        # c_sock.settimeout(time)
        try:
            data = c_sock.recv(BUFF_SIZE)
            print('Response', data.decode())
            break
        except timeout:
            time.sleep(1)
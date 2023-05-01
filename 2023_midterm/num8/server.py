from socket import *

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))

while True:
    message = [[]for _ in range(100)]
    while True:
        msg = c_sock.recv(BUFF_SIZE)
        temp = msg.decode()
        if temp == 'quit':
            break
        a , b = temp.split(" ",1) #공백 1개까지만 나누고 나머지는 그냥 처리
        if a == 'send':
            b,c = b.split(" ",1)
            index = int(b)-1
            message[index].append(c)
            result = "OK"
        
        elif a == 'receive':
            index = int(b)-1
            if message[index]:
                result = message[index][0]
                message[index].pop(0)
            else:
                result = "No messages"

        for i in range(10):
            time = 0.1
            data = result
            while True:
                c_sock.send(data.encode())
                print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
                c_sock.settimeout(time)
                try:
                    data = c_sock.recv(BUFF_SIZE)
                except timeout:
                    time *= 2
                    if time > 2.0:
                        break
                else:
                    print('Response', data.decode())
                    break
    c_sock.close()
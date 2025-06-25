import socket, select
import random

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('',PORT))
s_sock.listen(5)

socks.append(s_sock)

print(str(PORT) + ' 에서 접속 대기 중')

while True:
    r_scok, w_sock, e_sock = select.select(socks,[],[])

    for s in r_scok:
        if s == s_sock:
            c_sock ,addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data = s.recv(BUFFER)
            if not data:
                s.close()
                socks.remove(s)
                continue
            
            elif data == b'1':
                temp = random.randint(0,40)
                msg = f'Temp={temp}'
                s.send(msg.encode())
            elif data == b'2':
                humid = random.randint(0,100)
                msg = f'Humid={humid}'
                s.send(msg.encode())

            print('Received:', data.decode())
            
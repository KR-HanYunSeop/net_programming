import socket
import time

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 2500))

print('Server Started')

while True:
    data, addr = s.recvfrom(1024)
    # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove()
            continue
    
    # 새로운 클라이언트에면 목록에 추가
    if addr not in clients:
        print('new client', addr)
        clients.append(addr)

    print(time.asctime() + str(addr) + ':' + data.decode())

    for client in clients:
        if clients != addr:
            s.sendto(data, client)
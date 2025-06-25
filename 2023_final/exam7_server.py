import socket
import select
import threading
import time

socks = []
PORT = 2500
BUF_SIZE = 1024

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    # 읽기 이벤트(연결요청 및 데이터수신) 대기
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    for s in r_sock: # 수신(읽기 가능한) 소켓 리스트 검사
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock) # 연결된 클라이언트 소켓을 소켓 리스트에 추가 
            print('Client ({}) connected'.format(addr))
        else: # 기존 클라이언트의 데이터 수신 이벤트 발생 
            data = s.recv(BUF_SIZE)
            if 'quit' in data.decode() and sock in socks:
                print(addr, ': exited')
                socks.remove(sock)
                continue

            print(time.asctime() + str(addr) + ':' + data.decode())

            for x in clients:
                if x != sock:
                    x.send(data)

            if not data:
                s.close()
                socks.remove(s) # 연결 종료된 클라이언트 소켓을 소켓 리스트에서 제거 
                continue
            print('Received:', data.decode())
            s.send(data)

def server_task(sock, addr):
    while True:
        data = sock.recv(BUF_SIZE)

        if 'quit' in data.decode() and sock in clients:
            print(addr, ': exited')
            clients.remove(sock)
            continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        for x in clients:
            if x != sock:
                x.send(data)




while True:
    conn, addr = s.accept()
    clients.append(conn)
    print(conn, ': connected')
    threading.Thread(target=server_task, args=(conn, addr)).start()
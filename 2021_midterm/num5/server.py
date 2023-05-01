from socket import *

port = 6666
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',port))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    # print(conn,addr)
    message = [[]for _ in range(100)]
    while True:
        msg = conn.recv(BUFFSIZE)
        temp = msg.decode()
        if temp == 'quit':
            break
        a , b = temp.split(" ",1) #공백 1개까지만 나누고 나머지는 그냥 처리
        if a == 'send':
            b,c = b.split(" ",1)
            index = int(b)-1
            message[index].append(c)
            conn.send("Ok".encode())
        elif a == 'receive':
            index = int(b)-1
            if message[index]:
                rem = message[index][0]
                conn.send(rem.encode())
                message[index].pop(0)
            else:
                conn.send("No messages".encode())

    conn.close()
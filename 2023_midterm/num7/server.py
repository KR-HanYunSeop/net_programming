from socket import *
import os
import random

BUF_SIZE = 1024
LENGTH = 4 # 파일 크기 = 4바이트

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9999))
s.listen(10)

conn, addr = s.accept()
confirm = "Hello"
socket.send(confirm.encode())

while True:
    msg = conn.recv(BUF_SIZE).decode()
    if msg == '1':
        sender = random.randint(1, 50000)
        receiver = random.randint(1, 50000)
        lumi = random.randint(1, 100)
        humi = random.randint(1, 100)
        temp = random.randint(1, 100)
        air =random.randint(1, 100)
        seq = random.randint(1, 100000)
        result = f"Sender: {sender}, Receiver:{receiver}, Lumi:{lumi}, Humi:{humi}, Temp:{temp}, air:{air}, Seq:{seq}"
        print(result)
        conn.send(result.encode())

    elif msg.lower() == 'quit':
        print("Bye Bye")
        break
    
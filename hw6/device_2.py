from socket import *
import os
import random

BUF_SIZE = 1024
LENGTH = 4 # 파일 크기 = 4바이트

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(10)

conn, addr = s.accept()

while True:
    msg = conn.recv(BUF_SIZE).decode()
    if msg.lower() == '2':
        heartbeat = random.randint(40, 140)
        step = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        device2_result = f"Heartbeat={heartbeat}, Steps={step}, Cal={cal}"
        print(device2_result)
        conn.send(device2_result.encode())

    elif msg.lower() == 'quit':
        print("Bye Bye")
        break
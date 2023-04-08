from socket import *
import os
import random

BUF_SIZE = 1024
LENGTH = 4 # 파일 크기 = 4바이트

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(10)

conn, addr = s.accept()

while True:
    msg = conn.recv(BUF_SIZE).decode()
    if msg == '1':
        temperature = random.randint(0, 40)
        humid = random.randint(0, 100)
        bright = random.randint(70, 150)
        device1_result = f"Temp={temperature}, Humid={humid}, lilum={bright}"
        print(device1_result)
        conn.send(device1_result.encode())

    elif msg.lower() == 'quit':
        print("Bye Bye")
        break
    
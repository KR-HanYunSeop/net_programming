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
    if msg == '1':
        temp = random.randint(1, 50)
        humid = 0
        lumi = 0
        result = f"Temp={temp}, Humid={humid}, Lumi={lumi}"
        print(result)
        conn.send(result.encode())
    elif msg == '2':
        temp = 0
        humid = random.randint(1, 100)
        lumi = 0
        result = f"Temp={temp}, Humid={humid}, Lumi={lumi}"
        print(result)
        conn.send(result.encode())
    elif msg == '3':
        temp = 0
        humid = 0
        lumi= random.randint(1, 150)
        result = f"Temp={temp}, Humid={humid}, Lumi={lumi}"
        print(result)
    conn.send(result.encode())

    
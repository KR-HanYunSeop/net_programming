from socket import *
import datetime

device1_s = socket(AF_INET, SOCK_STREAM)
device2_s = socket(AF_INET, SOCK_STREAM)
device1_addr = ('localhost', 7777)
device2_addr = ('localhost', 8888)

device1_s.connect(device1_addr)
device2_s.connect(device2_addr)

while True:
    msg = input("Enter msg: ")
    f = open('data.txt', 'a')
    if msg == '1':
        device1_s.send(msg.encode())
        now = datetime.datetime.now()
        formatted_time = now.strftime("%a %b %d %H:%M:%S %Y: ") # 현재 날짜 및 시간 포맷팅
        data = device1_s.recv(1024).decode()
        result = formatted_time + "Device 1: " + data + "\n"
        print(result)
        f.write(result)
    elif msg == '2':
        device2_s.send(msg.encode())
        now = datetime.datetime.now()
        formatted_time = now.strftime("%a %b %d %H:%M:%S %Y: ") # 현재 날짜 및 시간 포맷팅
        data = device2_s.recv(1024).decode()
        result = formatted_time + "Device 2: " + data + "\n"
        print(result)
        f.write(result)
    elif msg == 'quit':
        device1_s.send(msg.encode())
        device2_s.send(msg.encode())
        break

    f.close()

device1_s.close()
device2_s.close()
        

from socket import *

s = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 8888)

s.connect(addr)

while True:
    msg = input("Enter msg: ")
    if msg == '1':
        s.send(msg.encode())
        data = s.recv(1024).decode()
        result = data + "\n"
        print(result)
    elif msg == '2':
        s.send(msg.encode())
        data = s.recv(1024).decode()
        result = data + "\n"
        print(result)
    elif msg == '3':
        s.send(msg.encode())
        data = s.recv(1024).decode()
        result = data + "\n"
        print(result)
    
    s.close()

        

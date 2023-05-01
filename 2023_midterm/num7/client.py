from socket import *

s = socket(AF_INET, SOCK_STREAM)

addr = ('localhost', 9999)

s.connect(addr)

confirm = s.recv(1024).decode()
print(confirm)


while True:
    msg = input("Enter msg: ")
    if msg == '1':
        s.send(msg.encode())
        data = s.recv(1024).decode()
        result = data + "\n"
        print(result)

    
    elif msg == 'quit':
        s.send(msg.encode())
        break


s.close()

        

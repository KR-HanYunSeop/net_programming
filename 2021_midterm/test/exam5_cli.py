import socket

port = 2500
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', port))

while True:
  msg = input("Enter the message('send mboxId message' or 'receive mboxId') : ")  
  s.send(msg.encode())
  if msg == 'quit':
    break
    
  data = s.recv(BUFSIZE)
  print(data.decode())

s.close()
import socket

port = 2500
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', port))

while True:
  msg = input("Messege to send : ")
  s.send(msg.encode())
  data = s.recv(BUFSIZE)
  print(data.decode())

s.close()
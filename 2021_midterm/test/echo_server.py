import socket
import time

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print('connecte by ', remotehost, remoteport)

while True:
  data = conn.recv(BUFSIZE)
  print("Received message : ", data.decode())
  conn.send(time.ctime(time.time()).encode())
  
conn.close()
sock.close()
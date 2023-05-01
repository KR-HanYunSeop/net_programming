import socket
import time

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
print("listen..!")

conn, (remotehost, remoteport) = sock.accept()
print('connecte by ', remotehost, remoteport)

mbox_dict = {}
while True:
  message = conn.recv(BUFSIZE)
  print("Received message : ", message.decode())
  
  message = message.decode()
  if message == 'quit':
    conn.close()
    conn, (remotehost, remoteport) = sock.accept()
    print('connecte by ', remotehost, remoteport)
    continue
  elif message.startswith("send "):
      mbox_id, mbox_message = message[5:].split(" ", 1)
      if mbox_id in mbox_dict:
          mbox_dict[mbox_id].append(mbox_message)
      else:
          mbox_dict[mbox_id] = [mbox_message]
      conn.sendall(b"ok")
  elif message.startswith("receive "):
      mbox_id = message[8:].strip()
      if mbox_id in mbox_dict:
        if not mbox_dict[mbox_id]:
          conn.sendall(b"no message")
        else:
          message_to_send = mbox_dict[mbox_id][0]
          conn.sendall(message_to_send.encode())
          # mbox_dict[mbox_id].pop(0)
          del mbox_dict[mbox_id][0]      
          print(mbox_dict[mbox_id])
      else:
        conn.sendall(b"no message")
  
conn.close()
sock.close()
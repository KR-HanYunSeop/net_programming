from socket import *
import random
from time import *


BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(10)

conn, addr = sock.accept()
msg = conn.recv(BUF_SIZE)
if not msg:
    conn.close()
elif msg == b'Register':
    print('client: ', addr, msg.decode())

    while True:
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)

        conn.send(f'{temp}/{humid}/{illum}'.encode())
        sleep(3)
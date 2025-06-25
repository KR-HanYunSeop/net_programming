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
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)

        conn.send(f'{heartbeat}/{steps}/{cal}'.encode())
        sleep(5)
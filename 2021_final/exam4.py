import selectors
import socket
import random

sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn,mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    elif data == b'1':
        temp = random.randint(0,40)
        msg = f'Temp={temp}'
        conn.send(msg.encode())
    elif data == b'2':
        humid = random.randint(0,100)
        msg = f'Humid={humid}'
        conn.send(msg.encode())

    print('received data:', data.decode())


sock = socket.socket()
sock.bind(('', 2501))
sock.listen(5)


sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
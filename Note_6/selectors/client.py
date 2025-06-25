from socket import *
import time
import selectors

BUF_SIZE = 1024
LENGTH = 20

def read_device1(conn, mask):
    msg = conn.recv(BUF_SIZE)
    temp, humid, illum = msg.decode().split('/')
    now = time.strftime('%c', time.localtime(time.time()))
    string = now + f': Device1: Temp={temp}, Humid={humid}, Illum={illum}\n'
    print(string)
    f = open('data.txt', 'a')
    f.write(string)
    f.close()


def read_device2(conn, mask):
    msg = conn.recv(BUF_SIZE)
    heartbeat, steps, cal = msg.decode().split('/')
    now = time.strftime('%c', time.localtime(time.time()))
    string = now + f': Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n'
    print(string)
    f = open('data.txt', 'a')
    f.write(string)
    f.close()

device1_socket = socket(AF_INET, SOCK_STREAM)
device1_socket.connect(('localhost', 7777))

device2_socket = socket(AF_INET, SOCK_STREAM)
device2_socket.connect(('localhost', 9999))

device1_socket.send(b'Register')
device2_socket.send(b'Register')

sel = selectors.DefaultSelector()
sel.register(device1_socket, selectors.EVENT_READ, read_device1)
sel.register(device2_socket, selectors.EVENT_READ, read_device2)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
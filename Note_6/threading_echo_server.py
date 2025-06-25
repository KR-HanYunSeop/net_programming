from socket import *
import threading

port = 2500
BUFSIZE = 1024

def echoTask(sock): # threading.Thread 클래스
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print('Received message: ', data.decode())
        sock.send(data)

    sock.close()

class ClientThread(threading.Thread): # threading.Thread의 파생 클래스 이용
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    
    def run(self):
        while True:
            data = self.sock.recv(BUFSIZE)
            if not data:
                break
            print('Received message: ', data.decode())
            self.sock.send(data)
        self.sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('conneted by', remotehost, remoteport)
    th = threading.Thread(target=echoTask, args=(conn,)) # threading.Thread 클래스
    th = ClientThread(conn) # threading.Thread의 파생 클래스 이용
    th.start()
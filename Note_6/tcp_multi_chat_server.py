import socket
import threading
import time

class ClientThread(threading.Thread):
    def __init__(self, conn, addr, clients):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.clients = clients

    def run(self):
        self.clients.append(self.conn)
        print('new client', self.addr)

        while True:
            data = self.conn.recv(1024)
            if not data:
                break

            message = data.decode()
            print(time.asctime() + str(self.addr) + ':' + message)

            #모든 클라이언트에게 전송
            for client in self.clients:
                if client != self.conn:
                    client.send(message.encode())

        print(self.addr,'exited')
        self.clients.remove(self.conn)
        self.conn.close()

if __name__ == '__main__':
    clients = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',2500))
    s.listen(1)

    print('Server Started')

    while True:
        conn, addr = s.accept()
        client_thread = ClientThread(conn, addr, clients)
        client_thread.start()
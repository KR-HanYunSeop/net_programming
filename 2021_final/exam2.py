from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from socket import *

port = 2500
BUFFSIZE = 1024

clients = []

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()

    def route(self):
        if self.path == '/':
            self.send_image()
        else:
            self.response(404, 'Not Found')

    def send_image(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        with open('iot.png', 'rb') as f:
            msg = f.read()
            self.wfile.write(msg)

    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(body.encode())

class ClientThread(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        while True:
            pass  # Add your client thread logic here

def serve_http():
    httpd = HTTPServer(('localhost', 8080), HTTPHandler)
    print('Serving HTTP on {}:{}'.format('localhost', 8080))
    httpd.serve_forever()

def serve_tcp():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)

    while True:
        conn, (remotehost, remoteport) = sock.accept()
        print('connected by', conn, remotehost, remoteport)
        th = threading.Thread(target=handle_tcp_request, args=(conn,))
        th.start()

def handle_tcp_request(conn):
    data = conn.recv(BUFFSIZE).decode()
    print('Received data:', data)

    # Create the HTTP response
    response = 'HTTP/1.1 200 OK\r\n'
    response += 'Content-type: image/png\r\n'
    response += '\r\n'
    with open('iot.png', 'rb') as f:
        msg = f.read()
        response += msg.decode()

    # Send the response over TCP
    conn.sendall(response.encode())

    # Close the TCP connection
    conn.close()

if __name__ == '__main__':
    http_thread = threading.Thread(target=serve_http)
    http_thread.start()

    tcp_thread = threading.Thread(target=serve_tcp)
    tcp_thread.start()

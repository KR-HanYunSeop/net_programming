import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # GET 요청 처리 로직 작성
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

    def do_POST(self):
        # POST 요청 처리 로직 작성
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"POST request received!")


class ThreadedHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    server_address = ('', 8000)
    server = ThreadedHTTPServer(server_address, MyHandler)

    # 멀티스레딩 서버 실행
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print('Server started on port 8000')

    # 다른 작업 수행

    server.shutdown()
    server_thread.join()

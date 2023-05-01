import socket

# 릴레이 서버 포트 번호
relay_port = 9000

# 외부 서버 및 포트 번호
target_host = "www.daum.net"
target_port = 80

# 릴레이 서버 소켓 생성
relay_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
relay_socket.bind(('localhost', relay_port))
relay_socket.listen(1)

print(f"Relay server is listening on port {relay_port}...")

while True:
    # 브라우저와의 연결 수립
    browser_conn, browser_addr = relay_socket.accept()
    print(f"Connected from {browser_addr}")

    # HTTP 요청 메시지 수신
    http_request = browser_conn.recv(4096).decode()
    print("HTTP request message from browser:")
    print(http_request)

    # 외부 서버에 대한 소켓 연결 수립
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_host, target_port))

    # 요청 라인과 Host 헤더만 추출하여 전송
    request_line = http_request.split("\r\n")[0]
    host_header = f"Host: {target_host}\r\n"
    target_socket.send((request_line + "\r\n" + host_header + "\r\n").encode())

    # 외부 서버에서 반환된 HTTP 응답 수신 및 전송
    http_response = target_socket.recv(4096)
    browser_conn.send(http_response)

    # 연결 종료
    target_socket.close()
    browser_conn.close()

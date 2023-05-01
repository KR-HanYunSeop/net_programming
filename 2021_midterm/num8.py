import socket

host = 'localhost'
port = 9005

#클라이언트와 통신할 소켓
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#클라이언트와 통신할 소켓
client_socket.bind((host, port))

client_socket.listen()

print("릴레이 서버는 브라우저를 기다리고 있습니다.")

while True :
    client_conn, client_addr = client_socket.accept()
    print("릴레이 서버와 브라우저가 연결되었습니다.")   #여기까지 잘되는거 확인함
    
    #브라우저로부터 HTTP 요청을 받아서 외부 서버에 전달 할 준비
    request_data = client_conn.recv(4096).decode("utf-8")
    if not request_data:
        continue
    
    #필요 부분만 뽑아내는 과정
    #GET / HTTP/1.1
    request_data = request_data.split("\r\n")
    request_data = request_data[0]
    print(request_data)         #결과    #GET / HTTP/1.1

    
    
    #외부서버에게 HTTP 메시지 전송
    exhost = "www.daum.net"
    send_external_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_external_server.connect(("www.daum.net", 80))
    send_external_server.sendall(f"{request_data}\r\nHost: {exhost}\r\n\r\n".encode("utf-8"))
    
    #외부 서버로부터 HTTP 응답 받아서 브라우저에게 전송
    response_data = send_external_server.recv(4096)    #decode할 필요 없음 브라우저에게 재전송
    if not response_data:
        continue
    client_conn.send(response_data)
    
    #소켓 종료
    send_external_server.close()
    client_conn.close()
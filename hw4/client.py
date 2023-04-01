import socket

port = int(input("Port No: "))
address = ('localhost', port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    # 사용자로부터 계산식 입력받기
    calculation = input("계산식을 입력하세요: ")
    
    # 'q'를 입력하면 종료
    if calculation == 'q':
        break
        
    # 계산식 서버로 전송
    s.sendall(calculation.encode())

    # 서버로부터 결과 받기
    result = s.recv(BUFSIZE).decode()

    # 결과 출력
    if '.' in result:
        result = float(result)
    else:
        result = int(result)
    
    print("계산 결과: ", result)

s.close()

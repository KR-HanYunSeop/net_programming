import socket

port = int(input("Port No: "))
address = ('localhost', port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(1)

print("Start Server...")

while True:
    conn, addr = s.accept()
    print("Client Access:", addr)
    
    while True:
        # 클라이언트로부터 계산식 받기
        calculation = conn.recv(BUFSIZE).decode()
        print(calculation)

        # 'q'를 입력하면 종료
        if calculation == 'q':
            conn.close()
            break

        # 계산
        if '+' in calculation:
            calculation = calculation.split('+')
            x,y = calculation
            result = str(int(x)+int(y))
        elif '-' in calculation:
            calculation = calculation.split('-')
            x,y = calculation
            result = str(int(x)-int(y))
        elif '*' in calculation:
            calculation = calculation.split('*')
            x,y = calculation
            result = str(int(x)*int(y))
        elif '/' in calculation:
            calculation = calculation.split('/')
            x,y = calculation
            result = str(round(int(x)/int(y),1))

        # 계산 결과 클라이언트로 전송
        conn.sendall(str(result).encode())

    conn.close()

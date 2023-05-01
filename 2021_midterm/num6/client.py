from socket import *

port = 2500
BUFFSIZE = 1024
sock = socket(AF_INET,SOCK_DGRAM)
sock.connect(('localhost',port))

time = 1
counter = 0
while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    while True:
        sock.send(msg.encode())
        sock.settimeout(time)  # 메세지를 보내고 타임아웃 걸기
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:        # time = 1이므로 1초 간격으로 
            counter+=1
            if counter > 3:    # 3회 재전송 (counter = 0, 1, 2)
                print("loss")
                counter = 0
                break
        else:
            print('Server says: ', data.decode())
            break
            
sock.close()
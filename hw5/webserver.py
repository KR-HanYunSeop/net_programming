from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    conn, addr = s.accept()

    data = conn.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    path = req[0].split(" ")
    path = path[1]
    filename = path[1:]

    if filename == "index.html":
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        response = 'Content-Type: ' + mimeType + '\r\n'
        conn.send(b'HTTP/1.1 200 OK\r\n')
        conn.send(response.encode())
        conn.send(b'\r\n')
        data = f.read()
        conn.send(data.encode('euc-kr'))
        conn.close()
        
    elif filename == "iot.png":
        f = open(filename, 'rb')
        mimeType = 'image/png'
        response = 'Content-Type: ' + mimeType + '\r\n'
        conn.send(b'HTTP/1.1 200 OK\r\n')
        conn.send(response.encode())
        conn.send(b'\r\n')
        data = f.read()
        conn.send(data)
        conn.close()

    elif filename == "favicon.ico":
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        response = 'Content-Type: ' + mimeType + '\r\n'
        conn.send(b'HTTP/1.1 200 OK\r\n')
        conn.send(response.encode())
        conn.send(b'\r\n')
        data = f.read()
        conn.send(data)
        conn.close()

    else:
        content = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n{}'.format(content)
        conn.send(response.encode())

        conn.close()

s.close()
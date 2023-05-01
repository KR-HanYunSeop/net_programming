import socket
import binascii
import sys

ip = "220.69.189.125"
port = 443

# A
tmp = socket.gethostbyaddr(ip)
hostname = tmp[0]
print(hostname)

# B
protocol = socket.getservbyport(port)
print(protocol)

# C
url = protocol + '://' + hostname
print(url)

# D
packed = socket.inet_aton(ip)
print(packed)
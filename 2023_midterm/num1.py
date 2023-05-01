str = "Hello, IoT"

# A
print(str * 3)

# B
print(str[0:4])

# C
print(str[-4:])

# D
print(str.lower())

# E
reverse = ""
count, i = 0, 0
count = len(str)

for i in range(0, count):
    reverse += str[count - (i + 1)]

print(reverse)
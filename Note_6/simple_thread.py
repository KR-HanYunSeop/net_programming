import threading

def prtSquare(num):
    print("Square : {}".format(num**2))

def prtCube(num):
    print("Cube : {}".format(num**3))

t1 = threading.Thread(target=prtSquare, args=(10,))
t2 = threading.Thread(target=prtCube, args=(10,))

t1.start() # start thread
t2.start()

t1.join # wait until thread 1 is completed
t2.join 

print("Done !")

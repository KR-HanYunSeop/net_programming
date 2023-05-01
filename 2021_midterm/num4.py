class MyComplex:
    def __init__(r, real, imaginary) :
        r.real = real
        r.imaginary = imaginary

    def multiply(r,i) :
        real = r.real * i.real - r.imaginary * i.imaginary
        imaginary = r.real*i.imaginary+r.imaginary*i.real
        print(f'{real}+{imaginary}i') #f는 출력값을 원소로 바꿈
        
        

a = MyComplex(3,-4)
b = MyComplex(-5,2)

a.multiply(b)

class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return MyComplex(real_part, imaginary_part)

a = MyComplex(3, -4)
b = MyComplex(-5, 2)

result = a * b

print(result.real, "+", result.imaginary, "i")

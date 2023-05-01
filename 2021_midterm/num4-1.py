class MyComplex:
    def __init__(self,real_1,imaginary_1,real_2,imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2

    def x(self):
        temp_real = (self.real_1 * self.real_2) - (self.imaginary_1 * self.imaginary_2)
        temp_imaginary = (self.real_1*self.imaginary_2 + self.real_2 * self.imaginary_1)
        if temp_imaginary < 0:
            temp_imaginary = '-'+str(temp_imaginary)+'i'
        else:
            temp_imaginary = '+'+str(temp_imaginary)+'i'
        result = (str(temp_real)+temp_imaginary)
        print(result)


if __name__ == '__main__' :
    mycom = MyComplex(3,-4,-5,2)
    mycom.x()
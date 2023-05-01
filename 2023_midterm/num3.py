class MyComplex:
    def __init__(self,real_1,imaginary_1,real_2,imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
    
    def add(self):
        temp_real = (self.real_1 + self.real_2)
        temp_imaginary = (self.imaginary_1 + self.imaginary_2)

        if temp_imaginary < 0:
            result = str(temp_real)+"-"+str(temp_imaginary)+"i"
        
        else:
            result = str(temp_real)+"+"+str(temp_imaginary)+"i"
        print(result)

    def minus(self):
        temp_real = (self.real_1 - self.real_2)
        temp_imaginary = (self.imaginary_1 - self.imaginary_2)

        if temp_imaginary < 0:
            result = str(temp_real)+str(temp_imaginary)+"i"
        
        else:
            result = str(temp_real)+"+"+str(temp_imaginary)+"i"
        print(result)

if __name__ == '__main__' :
    mycom = MyComplex(2,-3,-5,4)
    mycom.add()
    mycom.minus()
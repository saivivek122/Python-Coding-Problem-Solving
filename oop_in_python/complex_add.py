class complex_add():

    def read_complex(self):
        self.real = int(input("enter real part "))
        self.imag = int(input("enter imag "))

    def display_complex(self):
        print("The complex number is ",self.real, "+",self.imag,"i", sep="")

    def add_complex(self, complex1, complex2):
        self.real = complex1.real + complex2.real
        self.imag = complex1.imag + complex2.imag


c1 = complex_add()
c2 = complex_add()
c3 = complex_add()
print("enter first complex number")
c1.read_complex()
c1.display_complex()
print("enter second complex")
c2.read_complex()
c2.display_complex()
c3.add_complex(c1,c2)
c3.display_complex()

class complex_adder:

    def read_complex(self):
        self.real = int(input("enter real part"))
        self.img = int(input("enter img part"))

    def display_complex(self):
        print("complex number is ",self.real,"+",self.img,"i")

    def complex_addition(self, c1, c2):
        self.real = c1.real + c2.real
        self.img = c1.img + c2.img


c1 = complex_adder()
c2 = complex_adder()
c3 = complex_adder()
print("enter first complex number ")
c1.read_complex()
c1.display_complex()
print("enter second complex")
c2.read_complex()
c2.display_complex()
c3.complex_addition(c1,c2)
c3.display_complex()
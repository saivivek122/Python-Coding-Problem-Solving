num = int(input("enter first"))
second = int(input("enter second"))


class Addition:
    def __init__(self,k,p):
        self.num = num
        self.second = second

    def adder(self):
        return self.num + self.second


a1 = Addition(num, second)
print(a1.adder())

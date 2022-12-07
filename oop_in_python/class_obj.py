class computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config are", self.cpu, self.ram)


comp1 = computer('i5', 16)
comp2 = computer('i10', 4)
comp1.config()
comp2.config()

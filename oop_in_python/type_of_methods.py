# Types of methods Python function
class Student:
    school = "SR"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod  # It is class method
    def get_school_name(cls):
        return cls.school

    @staticmethod  # static method not related to any other objects or instances
    def add_number(a, b):
        return a + b


s1 = Student(12, 23, 34)

s2 = Student(13, 33, 45)

print(s1.get_avg())
print(s2.get_school_name())
print(Student.add_number(3, 5))

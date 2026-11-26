class Student:
    s = 5

    @classmethod
    def display(cls):
        print(f"The value of class attribute is {cls.s}")

ob = Student()
ob.s = 10
ob.display()
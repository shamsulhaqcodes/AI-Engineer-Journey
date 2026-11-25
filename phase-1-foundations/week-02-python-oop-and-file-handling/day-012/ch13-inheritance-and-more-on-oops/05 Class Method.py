class Employee:
    a = 7
    @classmethod
    def show(cls):
        print(f"The class attribute a is {cls.a}")  

e = Employee()
e.a = 45

e.show()
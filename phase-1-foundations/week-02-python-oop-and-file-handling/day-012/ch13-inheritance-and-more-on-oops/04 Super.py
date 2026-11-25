class Employee:
    def __init__(self):
        print("Consturctor of Emoployee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        # super().__init__()
        print("Consturctor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Consturctor of Manager")
    c = 3

# o = Employee()
# print(o.a)            # Prints the a attribute
# # print(o.b)         # Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)
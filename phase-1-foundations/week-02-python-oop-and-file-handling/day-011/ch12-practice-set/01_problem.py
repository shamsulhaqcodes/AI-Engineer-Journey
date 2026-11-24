# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin 

p1 = Programmer("Shamsulhaq", 500000, 85223)
print(f"Name: {p1.name}\nPin: {p1.pin}\nSalary: {p1.salary}\nCompany: {p1.company} ")

p2 = Programmer("Raza", 700000, 98423)
print(f"\nName: {p2.name}\nPin: {p2.pin}\nSalary: {p2.salary}\nCompany: {p2.company} ")

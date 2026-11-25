class Employee:
    company = "Google"
    name = "Ali"
    def displayInfo(self):
        print(f"The name of employee is {self.name}\nThe salary of employee is {self.company}")

class Coder:
    language = "python"
    def showlanguage(self):
        print(f"The language of this employee is {self.language}")

class Programmer(Employee , Coder):     # Multiple Inheritance 
    company = "Microsoft"
    salary = "20k"
    def display(self):
        print(f"The name of employee is {self.company}\nThe salary of employee is {self.salary}")

a = Employee()
b = Programmer()
# print(a.company)
# print(b.company)

b.displayInfo()
b.showlanguage()
b.display()
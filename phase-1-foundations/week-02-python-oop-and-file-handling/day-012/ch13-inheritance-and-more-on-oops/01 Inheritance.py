class Employee:
    company = "Google"
    def displayInfo(self):
        print(f"The name of employee is {self.name}\nThe salary of employee is {self.salary}")

# class Programmer:
#     company = "Microsoft"
#     def displayInfo(self):
#         print(f"The name of employee is {self.name}\nThe salary of employee is {self.salary}")
#     def showLanguage(self):
#         print(f"The language of this employee is {self.Language}")
class Programmer(Employee):     # Single Inheritance 
    company = "Microsoft"
    def displayInfo(self):
        print(f"The name of employee is {self.name}\nThe salary of employee is {self.salary}")

a = Employee()
b = Programmer()
print(a.company)
print(b.company)
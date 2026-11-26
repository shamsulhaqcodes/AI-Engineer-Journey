class Employee:
    company = "Microsoft"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def info(self):
        print(f"Name of Employee: {self.name}\nSalary of Employee: {self.salary}")

# class Programmer:
#     company = "Microsoft Dev"
#     def __init__(self, name, salary, language):
#         self.name = name
#         self.salary = salary
#         self.language = language

#     def info(self):
#         print(f"Name of Employee: {self.name}\nSalary of Employee: {self.salary}")

#     def showLanguage(self):
#         print(f"Name of Employee: {self.name}\nSalary of Employee: {self.language}")

class Programmer(Employee):      # Single Inheritance
    company = "Microsoft Dev"
    def __init__(self, name, salary, language):
        super().__init__(name, salary)        # reuse Employee's __init__
        self.language = language

    def showLanguage(self):
        print(f"Language of Empolyee: {self.language}")

a = Employee("Ahamd", 300000)
b = Programmer("Shamsulhaq", 500000, "Python")

print(a.company)
print(b.company)

a.info()
b.info()
b.showLanguage()
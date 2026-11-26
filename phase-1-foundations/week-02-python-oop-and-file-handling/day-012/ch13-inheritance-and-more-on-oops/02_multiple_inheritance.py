class Employee:
    company = "Microsoft"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def info(self):
        print(f"Name of Employee: {self.name}\nSalary of Employee: {self.salary}")

class Coder:
    experience = "7 years"
    def codingExp(self):
        print(f"Coding Experience: {self.experience}")

class Programmer(Employee, Coder):      # Multiple Inheritance
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
b.codingExp()
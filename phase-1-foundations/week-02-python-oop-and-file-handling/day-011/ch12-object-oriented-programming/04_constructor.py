class Employee:          
    salary = 300000
    lang = "Python"     
    def getInfo(self):
        print(f"The language is {self.lang}. And the salary is {self.salary}.")

    def __init__(self, name, language, salary):   # dunder method which is automatically called
        self.name = name
        self.lang = language  # The left side is the object's own variable (an attribute).The right side is the parameter
        self.salary = salary

        print("A new object was created.")

    @staticmethod              
    def greet():
        print(f"Salam, Everyone")

ahmad = Employee("Ahmad", "Python", 300000) 
# ahmad.name = "Ahmad"
        
print(ahmad.name)
print(ahmad.lang)
print(ahmad.salary)
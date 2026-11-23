class Employee:          
    salary = 300000
    lang = "Javascript"     
    def getInfo(self):
        print(f"The language is {self.lang}. And the salary is {self.salary}.")

    # def greet(self):
    #     print(f"Salam, Everyone")

    @staticmethod              # static means don't need of self
    def greet():
        print(f"Salam, Everyone")

ahmad = Employee()         
ahmad.lang = "Python"                        # object/instance attribute
# print(ahmad.salary, ahmad.lang)

ahmad.getInfo()
# Employee.getInfo(ahmad)

ahmad.greet()
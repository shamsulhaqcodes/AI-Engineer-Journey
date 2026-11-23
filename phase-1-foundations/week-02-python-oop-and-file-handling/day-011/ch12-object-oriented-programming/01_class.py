class Employee:          # Simple exp of class Employee
    salary = 300000
    lang = "Python"     # salary and lang are class attributes as they directly belongs to class

ahmad = Employee          # Here ahmad is an object
ahmad.name = "Ahmad"
print(ahmad.name, ahmad.salary, ahmad.lang)

bilal = Employee
bilal.name = "Bilal"
print(bilal.name, bilal.lang, bilal.salary)

# Here name is a object/instance attribute
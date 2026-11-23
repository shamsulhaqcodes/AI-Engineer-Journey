class Employee:          
    salary = 300000
    lang = "Javascript"     

ahmad = Employee         
ahmad.name = "Ahmad"
ahmad.lang = "Python"                        # object/instance attribute
print(ahmad.name, ahmad.salary, ahmad.lang)

# Instance attributes, take preference over class attributes during assignment & retrieval.

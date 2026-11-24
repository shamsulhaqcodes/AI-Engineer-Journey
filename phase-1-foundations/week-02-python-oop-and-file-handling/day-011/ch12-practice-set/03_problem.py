# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 4

ob = Demo()
print(ob.a)  # print 4 because instance attribute is not present

ob.a = 0
print(ob.a)   # print 0 because instance attribute is present
print(Demo.a)  # ob.a = 0 not change the class attribute
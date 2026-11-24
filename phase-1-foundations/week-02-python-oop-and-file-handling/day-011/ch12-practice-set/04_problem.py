# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, num):
        self.n = num

    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")

    def cube(self):
        print(f"The square of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square of {self.n} is {self.n ** (1/2)}")

    @staticmethod
    def greet():
        print("Hello World")

a = Calculator(4)
b = Calculator(9)

b.squareroot()   # uses 9
a.squareroot()   # still uses 4

a.greet()

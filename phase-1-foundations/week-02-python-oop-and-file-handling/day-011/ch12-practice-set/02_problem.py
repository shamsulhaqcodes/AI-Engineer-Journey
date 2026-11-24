# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, num):
        self.n = num

    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")

    def cube(self):
        print(f"The square of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square of {self.n} is {self.n ** (1/2)}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()

b = Calculator(9)
b.squareroot()   # uses 9
a.squareroot()   # still uses 4
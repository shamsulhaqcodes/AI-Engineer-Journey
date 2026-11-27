# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self , r , i):
        self.r = r
        self.i = i

    def __add__(self , c2 ):
        return Complex(self.r + c2.r , self.i + c2.i)
    
    def __mul__(self, c2):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1 , 3)
c2 = Complex(5 , 8)

print(c1 + c2)
print(c1 * c2)

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return Complex(real, imag)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# # Test
# c1 = Complex(1, 3)
# c2 = Complex(5, 8)

# print("Addition:", c1 + c2)   # (1+5) + (3+8)i = 6 + 11i
# print("Multiplication:", c1 * c2)  # Using formula

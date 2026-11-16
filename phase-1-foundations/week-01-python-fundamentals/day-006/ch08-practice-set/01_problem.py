# Write a program using functions to find greatest of three numbers.

def greatest(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
print(f"The greatest number is {greatest(num1, num2, num3)}")

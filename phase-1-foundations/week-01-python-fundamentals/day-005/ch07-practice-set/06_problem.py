# Write a program to calculate the factorial of a given number using for loop.
# Factorial Formula:
# Factorial of n = n! = n × (n - 1) × (n - 2) × ... × 1

# Examples:
# 0! = 1
# 1! = 1
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 =  24

n = int(input("Enter the number until you want to sum: "))
factorial = 1
for i in range(1, n+1):
    factorial*=i
print(f"Factorial of {n} is {factorial}")
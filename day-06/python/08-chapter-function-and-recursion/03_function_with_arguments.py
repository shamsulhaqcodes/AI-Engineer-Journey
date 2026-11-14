def greet(name, ending):     # Here "name" and "ending" is a parameter
    print("Good Morning, " + name, ending)       # string concatination

greet("Hamza", "Sukriya")
greet("Ahmad", "Thanks")
greet("Shamsulhaq", "Thank you")


def sum_of_n(n):          # Return the sum of the first n natural numbers.
    total = 0
    for i in range(1, n + 1):
        total += i
    return total        # Function can do work, but return is how it hands a 
                        # result back to the code that called it.

n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a positive number.")
else:
    result = sum_of_n(n)
    print(f"The sum of the first {n} natural numbers is: {result}")
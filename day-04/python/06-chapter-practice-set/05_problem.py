# Write a program which finds out whether a given name is present in a list or not

list = ["Shamsulhaq", "Ali", "Ahamd", "Bilal", "Abdullah"]
name = input("Enter the name: ")
if(name in list):
    print(f"{name} is found")
else:
    print(f"{name} is not found")
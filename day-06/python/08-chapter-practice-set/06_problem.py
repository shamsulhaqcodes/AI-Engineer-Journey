# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    return inches * 2.54

inches = int(input("Enter Inches: "))
print(f"Centimeter = {inches_to_cms(inches)}")
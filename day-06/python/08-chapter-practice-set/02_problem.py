# Write a python program using function to convert Celsius to Fahrenheit.
# Formula:
# (0°C × 9/5) + 32 = 32°F

def cel_to_fahren(n):
    return (n*(9/5)) + 32

temp = int(input("Enter temprature in Celsius: "))
fahren = cel_to_fahren(temp)
print(f"Fahrenheit = {round(fahren, 2)}")
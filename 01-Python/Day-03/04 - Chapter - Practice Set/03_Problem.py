# Check that a tuple type cannot be changed in python

tuple = ("Shams", 100, True)
tuple[2] = False     # displays error because tuple is immutable
print(tuple)
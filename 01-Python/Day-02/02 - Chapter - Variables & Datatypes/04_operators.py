print('Arithmetic Operators:')
a = 9
b = 3
print(a+b)       # (+) is an Arithmetic Operator
print(a-b)       # (-) is an Arithmetic Operator
print(a*b)       # (*) is an Arithmetic Operator
print(a/b)       # (/) is an Arithmetic Operator

print('\nAssignment Operators:')
c = 3-2   # Assign (3-2) in c
print(c)
d = 5
d += 3   # Increment the value of d by 3 and assign it to d
print(d)
d -= 3   # Decrement the value of d by 3 and assign it to d
print(d)

print('\nComparison Operators:')  # Always return True or False (Boolean)
d = 5>8     # False
f = 19<99     # True
check = 87 <= 87   # True
check2 = 5!=5
check3 = 5==5
print(d, f, check, check2, check3)

print('\nLogical Operators:')  # (and | or | not)
l = True or False

print("Truth Talbe of (or)") 
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True  is", False or True)
print("False or False is", False or False)

print("\nTruth Talbe of (and)")
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True  is", False and True)
print("False and False is", False and False)

print("\nNot Operaotr")
print(not(False))
print(not(True))
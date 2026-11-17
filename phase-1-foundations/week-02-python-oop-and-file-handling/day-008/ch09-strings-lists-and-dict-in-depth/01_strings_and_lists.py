for ch in "Python":   # (Strings almost done in week-01)
    print(ch)


l = [10, 20, 30, 40, 50, 60, 70]
for i, value in enumerate(l):
    print(f"{i} : {value}")           # index and value together


# Strings are immuteable

s = "hello"
# s[0] = "H"       # TypeError: strings can't be changed

s = "H" + s[1:]    # create a NEW string instead
print(s)           # Hello


# Lists are muteable
l = [10, 20, 30]
l[0] = 99
print(l)       # [99, 20, 30]  (same list, changed in place)

num = [3, 1, 2, 5, 4]
num.sort()
print(num)

num.sort(reverse=True)
print(num)
# num.reverse()
# print(num)

l2 = [3, 1, 2]

new = sorted(l2)     # Returns a new list, orignal unchanged
print(new)
print(l2)

''' Already covered in week 1'''
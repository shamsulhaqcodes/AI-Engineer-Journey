# Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []
f1 = (input("Enter the name of marks of first student: "))
marks.append(f1)
f2 = (input("Enter the name of marks of second student: "))
marks.append(f2)
f3 = (input("Enter the name of marks of third student: "))
marks.append(f3)
f4 = (input("Enter the nam of marks of fourth student: "))
marks.append(f4)
f5 = (input("Enter the name of marks of fith student: "))
marks.append(f5)
f6 = (input("Enter the name of marks of sixth student: "))
marks.append(f6)

marks.sort()
print(marks)
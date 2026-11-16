# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))
if(marks>90):
    print("Excellent")
elif(marks>80 or marks==90):
    print("Grade is A")
elif(marks>70 or marks==80):
    print("Grade is B")
elif(marks>=60 or marks==70):
    print("Grade is C")
elif(marks>=50 or marks==60):
    print("Grade is D")
else:
    print("Grade is F")
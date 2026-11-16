# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

math_marks = int(input("Enter the marks of Math: "))
eng_marks = int(input("Enter the marks of eng: "))
science_marks = int(input("Enter the marks of science: "))

total_percentage = (100*(math_marks+eng_marks+science_marks))/300
if(total_percentage>=40 and math_marks>=33 and science_marks>=33 and eng_marks>=33):
    print(f"You are Pass, Percentage = {total_percentage}")
else:
    print(f"You are Fail, Percentage = {total_percentage}")
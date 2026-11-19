# 7. Write a program to find out the line number where python is present from problem 06

with open("log.txt") as f:
    lines = f.readlines()

line_no = 1
for line in lines:
    if "Python" in line:
        print(f"Present in line {line_no}")
        break
    line_no +=1
else:
    print("Not Present")

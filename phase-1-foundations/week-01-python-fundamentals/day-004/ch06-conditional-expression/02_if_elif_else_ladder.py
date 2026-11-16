age = int(input("Enter your age: "))

if(age>=18):     # if-elif-ladder
    print("You are eligible to drive.")

elif(age<0):
    print("Invalid negative age!")

elif(age==0):
    print("0 is invalid age!")
        
else:
    print("You are not eligible to drive.")

print("Thank You!")  # End of Program
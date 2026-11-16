# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter you username: ")
if(len(username) < 10):
    print("Your username contain less than 10 characters")
else:
    print("Good")
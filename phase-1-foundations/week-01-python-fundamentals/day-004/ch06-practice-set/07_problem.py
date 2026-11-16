# Write a program to find out whether a given post is talking about "Ahmad" or not.

post = input("Enter your post: ")
if("Ahmad".lower() in post.lower()):
    print("Yes, it's talking about Ahmad.")
else:
    print("No, it's not talking about Ahmad.")
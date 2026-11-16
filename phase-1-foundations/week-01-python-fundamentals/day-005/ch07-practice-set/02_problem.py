# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Shamsulhaq", "Ahmad", "Sameer", "Murad", "Saif", "Kamran"]
for i in l:
    if(i.startswith("S")):
        print("Assalam o Alikum,", i)
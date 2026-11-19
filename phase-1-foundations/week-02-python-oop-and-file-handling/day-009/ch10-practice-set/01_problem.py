#  Write a program to read the text from a given file ‘poem.txt’ and find out whether it contains the word 'magic'.

with open("poem.txt") as f:
    data = f.read()
    if "magic" in data:
        print("magic is found")
    else:
        print("Not found")

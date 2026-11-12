# Write a python program to print the contents of a directory using the os module.

import os                      # Built-in Module in Python
folder = os.getcwd()          # get path of current working directory
items = os.listdir(folder)   # names of the list in dir

print("Contents of:", folder)
print(items)
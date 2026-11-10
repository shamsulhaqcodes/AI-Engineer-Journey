name = "Shamsulhaq"

nameshort = name[0:5]
print(nameshort)

namest = name[-7:-3]
print(namest)

namesht  = name[3:7]
print(namesht)

print(name[3:])  # From index 3 to End (3:11)
print(name[:5])  # From starting index to 5 (0:5)


str = "Slicing"
print(str[0:5:3])  # str[start : stop : step] ---> (Sc)


# Rule to remember: Make the jumps, but only keep the stones that are less than the stop.
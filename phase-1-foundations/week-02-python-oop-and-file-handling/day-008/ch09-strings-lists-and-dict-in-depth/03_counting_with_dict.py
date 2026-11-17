# Count numbers in a list

numbers = [100, 200, 400, 300, 200, 100, 300, 100]
count = {}    # Empty dict

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)


# Count characters in a string
# str = "Shamsulhaq"
count2 = {}

for ch in "Shamsulhaq":       # Python allows loop directly through a string
    if ch in count2:
        count2[ch] += 1
    else:
        count2[ch] = 1

print(count2)





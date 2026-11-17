# Find the first character that appears exactly once.

text = "aabbcdeeff"

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

for char in text:
    if count[char] == 1:
        print("First non-repeating character:", char)
        break

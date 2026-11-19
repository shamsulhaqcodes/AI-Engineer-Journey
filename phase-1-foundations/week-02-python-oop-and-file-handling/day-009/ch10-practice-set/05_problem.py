# Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "hate", 'bad']
with open("file.txt") as f:
    data = f.read()
for word in words:
    data = data.replace(word, "#" * len(word))
with open("file.txt", "w") as f:
    f.write(data)
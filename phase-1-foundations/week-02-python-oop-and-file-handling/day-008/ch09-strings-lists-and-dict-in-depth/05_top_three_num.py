sentence = "python is easy python is powerful python is useful"

words = sentence.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

top_three = sorted(
    count.items(),
    key=lambda item: item[1], # Sort according to the second element of each pair, which is the count
    reverse=True      # Sorts from highest to lowest
)[:3]

print(top_three)
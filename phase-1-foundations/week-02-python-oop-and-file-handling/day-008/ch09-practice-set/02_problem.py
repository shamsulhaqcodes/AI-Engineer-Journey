# Display the three most frequently appearing words in descending order.

sentence = "AI is powerful and AI is useful because AI helps people"
count = {}

words = sentence.lower().split()

for word in words:
    count[word] = count.get(word, 0) + 1

top_three = sorted(
    count.items(),           # here (items) is a buit-in function
    key= lambda item: item[1],
    reverse=True
)[:3]

print(top_three)
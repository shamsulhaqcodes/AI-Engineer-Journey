# Find the number that appears most frequently and its frequency.

numbers = [10, 20, 10, 30, 20, 10, 40, 20, 20]

count = {}
for num in numbers:
    count[num] = count.get(num, 0) + 1

most_frequent = max(count, key= count.get)

print(f"Frequency = {count}")
print(f"Most Frequent = {most_frequent}")
print(f"Number of Occurances = {count[most_frequent]}")

# Count items using get()

fruits = ["apple", "banana", "apple", "grapes", "apple", "banana", "orange"]
count = {}

for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1

print(count)




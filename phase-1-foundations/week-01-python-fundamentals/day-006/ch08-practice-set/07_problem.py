# Write a python function to remove a given word from a list and strip it at the same time.

l = ["Shamsulhaq", "Ali", "Hamza", "Farhan", "Rayan"]
print(l)

def remove_word(li, word):
    new_list = []
    for item in li:
        if (item != word):
            new_list.append(item.strip(word))
    return new_list

w = input("Enter a word, you want to remove: ")
nl = remove_word(l,w)
print(nl)

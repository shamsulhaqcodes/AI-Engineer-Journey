s = {1, 2, 3}

s.add(4)            # {1, 2, 3, 4}
print(s)

s.update([5, 6])    # {1, 2, 3, 4, 5, 6}  -> add many items
print(s)

s.remove(6)         # removes 6, raises KeyError if missing
s.discard(100)      # removes if present, NO error if missing
x = s.pop()         # removes and returns a random item
s.clear()           # empties the set -> set()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))                  # {1, 2, 3, 4, 5, 6}   also: a | b
print(a.intersection(b))           # {3, 4}               also: a & b
print(a.difference(b))             # {1, 2}               also: a - b
print(a.symmetric_difference(b))   # {1, 2, 5, 6}         also: a ^ b

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


s = {1, 2, 3}

s.add(4)            # {1, 2, 3, 4}
s.update([5, 6])    # {1, 2, 3, 4, 5, 6}  -> add many items

s.remove(6)         # removes 6, raises KeyError if missing
s.discard(100)      # removes if present, NO error if missing
x = s.pop()         # removes and returns a random item
s.clear()           # empties the set -> set()
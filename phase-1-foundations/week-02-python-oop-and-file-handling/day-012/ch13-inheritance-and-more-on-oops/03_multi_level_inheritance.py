class grandParent():
    gp = 1

class parent(grandParent):
    p = 2

class child(parent):
    c = 3

o1 = grandParent
o2 = parent
o3 = child

print(o1.gp)
# print(o1.p)    # Display an Error bez there is no p attribute in class

print(o2.p, o2.gp)
print(o3.c, o3.p, o3.gp)
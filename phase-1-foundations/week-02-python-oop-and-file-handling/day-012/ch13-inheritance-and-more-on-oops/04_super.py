class grandParent():
    def __init__(self):
        print("Constructor of Grand Parent.")
    gp = 1

class parent(grandParent):
    def __init__(self):
        print("Constructor of Parent.")
    p = 2

class child(parent):
    def __init__(self):
        super().__init__()
        print("Constructor of Child.")
    c = 3

# o1 = grandParent()
# o2 = parent()
o3 = child()


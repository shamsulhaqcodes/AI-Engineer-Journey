class Student:

    @property
    def name(self):
        return (f"Student Name: {self.name}")
        

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if(value < 0):
            print("Age cannot be negative")
        elif(value == 0):
            print("Age cannot be zero")
        else:
            self._age = value 
            print(f"Student age: {self._age}")

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

s = Student()
s.name = "Muhammad Shamsulhaq"

print(s.lname)
print(s.fname, s.lname)

s.age = -1
s.age = 0

s.age = 20
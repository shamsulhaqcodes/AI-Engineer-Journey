marks = {                
    "Ali":94,          
    "Bilal" : 78,
    "Shams": 100,
    "Usman" : 89
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Shams":99, "Haider":91})
print(marks)

print(marks.get["Shams2"])   # display None
print(marks["Shams2"])       # display Error

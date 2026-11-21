import json

students = {
    "Name": "Ali",
    "Age": 20, 
    "Passed": True, 
    "Grade": {"Python": "A+", "C++": "A", "Javascript": "B"},
    "Location": None
    }
text = json.dumps(students)  # Python ---> JSON string
print(text, type(text))

# JSON string ---> Python
back = json.loads(text)
print(back, type(back))

print(back["Name"], type(back))
print(back["Grade"]["Python"])

# indent=4 makes it readable, and sort_keys=True orders keys alphabetically
print(json.dumps(students, indent=4, sort_keys=True))

# with open("student.json", "w", encoding="utf-8") as f:
#     json.dump(students, f, indent=4)                         # write a file

with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)                                       # read a file
    print(loaded)
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Department", "Marks"])

    writer.writerow(["Ali", 21, "BSCS", 85])
    writer.writerow(["Shamsulhaq", 20, "BSCS", 90])
    writer.writerow(["Raza", 22, "BBA", 92])

print("CSV file created successfully!")

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

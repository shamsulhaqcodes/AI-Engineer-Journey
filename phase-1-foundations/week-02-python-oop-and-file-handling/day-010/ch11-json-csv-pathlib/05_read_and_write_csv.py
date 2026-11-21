import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Department", "Marks"])

    writer.writerow(["Ali", 21, "BSCS", 85])
    writer.writerow(["Ahmed", 22, "BSCS", 90])
    writer.writerow(["Sara", 20, "BBA", 92])

print("CSV file created successfully!")

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

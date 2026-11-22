from pathlib import Path

file_name = Path("03_nested_data.py")
print(file_name)
print(type(file_name))

print(Path.cwd())
print(Path.home())


file_path = Path("week-02-python-oop-and-file-handling/day-010/ch11-json-csv-pathlib/03_nested_data.py")

print("Name:", file_path.name)
print("Stem:", file_path.stem)
print("Suffix:", file_path.suffix)
print("Parent:", file_path.parent)

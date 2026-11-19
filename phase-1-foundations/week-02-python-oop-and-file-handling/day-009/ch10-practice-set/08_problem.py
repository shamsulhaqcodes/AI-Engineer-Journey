import os

old_name = "file.txt"                  # the file you want to rename
new_name = "renamed_by_python.txt"     # the new name

os.rename(old_name, new_name)
print(f"Renamed '{old_name}' to '{new_name}'")
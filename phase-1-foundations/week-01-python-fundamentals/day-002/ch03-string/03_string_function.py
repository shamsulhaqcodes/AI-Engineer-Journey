name = "Muhammad Shamsulhaq"
print(len(name))
print(name.endswith("haq"))
print(name.endswith("haqq"))
print(name.startswith("m"))
print(name.startswith("Mu"))
print(name.capitalize())
print(name.lower())


print(name.strip())     
print(name.lstrip())
print(name.rstrip())

# strip() removes spaces (and newlines) from both ends.
# lstrip is left only, and rstrip is right only. 
# It does not touch spaces in the middle.

print("I like Python".replace("like", "love"))

msg = "   HeLLo WoRLD  "
clean = msg.strip().lower().title()
print(clean)    # Hello World
# Write a program to generate multiplication tables from 2 to 50 and write it to the different files. Place these files in a folder for a 10 – year old

def table_genrator(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 51):
    table_genrator(i)

# import os

# def table_generator(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n * i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)

# os.makedirs("tables", exist_ok=True)   # 1) folder is created here

# for i in range(2, 21):                 # 2) only then do we write files
#     table_generator(i)
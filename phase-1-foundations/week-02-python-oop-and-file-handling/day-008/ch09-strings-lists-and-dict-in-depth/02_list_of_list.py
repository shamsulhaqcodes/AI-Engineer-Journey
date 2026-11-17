# Lists of lists (2D data)
# A list can hold any object, including other lists. A “list of lists” is a table: the outer list holds the rows, and each inner list is one row.

matrix = [[1, 2, 3],
         [4, 5, 6]]

# matrix[0]= 10
# print(matrix)

print(matrix[1][2])     # 6   (row 1, column 2)

for row in matrix:
    for value in row:
        print(value, end=" ")
    print("")


for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(f"matrix[{r}][{c}] = {matrix[r][c]}") 

m = [[1], [2, 3], [4, 5, 6]]
for row in m:
    print(len(row), row)

rows, cols = 2, 3
grid = [[0] * cols for _ in range(rows)]  # (_) it is a name for “a loop variable I don’t need”.
print(grid)   
 
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

# Using a for loop.

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed) # ---> [[1, 4], [2, 5], [3, 6], [4, 8]]

# Using list comprehension.

matrix = [[1, 2], [3,4], [5,6], [7,8]]

transposed = [[row[i] for row in matrix] for i in range(2)]

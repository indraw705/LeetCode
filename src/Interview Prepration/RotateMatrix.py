# Define a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix
transposed_matrix = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)

print(transposed_matrix)
# Reverse each row of the transposed matrix
rotated_matrix = []
for row in transposed_matrix:
    reversed_row = []
    for element in reversed(row):
        reversed_row.append(element)
    rotated_matrix.append(reversed_row)

# Print the rotated matrix
for row in rotated_matrix:
    print(row)

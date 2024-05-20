# Define a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = []

for i in range(len(matrix)):
    temp_list = []
    for row in matrix:
        temp_list.append(row[i])
    transpose_matrix.append(temp_list)

final_matrix = []
for row in transpose_matrix:
    temp_list = []
    for element in reversed(row):
        temp_list.append(element)
    final_matrix.append(temp_list)

for row in final_matrix:
    print(row)
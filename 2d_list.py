# 2d list means list with in a list

matrix =[
    [2, 4, 6],
    [56, 78, 2],
    [2, 6, 8]
]
print(matrix)
print(matrix[0])
print(matrix[0][2])
print(matrix[2])
matrix[2][2]=100
print(matrix[2][2])


for row in matrix:
    for item in row:
        print(item)
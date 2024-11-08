import pandas as pd

mat1 = [
    [9,0],
    [3,6]
]

mat2 = [
    [6,0],
    [7,2],
]

for  x in range(0,len(mat1)):
    for y in range(0,len(mat1[0])):
        print(mat1[x][y] + mat2[x][y], end=" "),
    print

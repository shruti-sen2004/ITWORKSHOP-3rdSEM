x= eval(input("ENETR 1ST MATRIX: "))
y= eval(input("ENETR 2ND MATRIX: "))

row_x= len(x)
col_x= len(x[0])

row_y= len(y)
col_y= len(y[0])

if col_x != row_y:
    print("MATRIX CANNOT BE MULTIPLIED!!")
else:
    result = [[0 for j in range(col_y)]for i in range(row_x)] #creates the matrix of row x*col y
    for i in range(row_x):
        for j in range(col_y):
            for k in range(row_y):
                result[i][j] += x[i][k] * y[k][j]
    print(result)

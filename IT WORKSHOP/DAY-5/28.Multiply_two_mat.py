X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

# Get the number of rows and columns in X
rows_X = len(X)
cols_X = len(X[0])

# Get the number of rows and columns in Y
rows_Y = len(Y)
cols_Y = len(Y[0])

# Check if the multiplication is valid
if cols_X != rows_Y:
    print("The matrices cannot be multiplied")
    exit()
# Create a result matrix with zeros
result = [[0 for j in range(cols_Y)] for i in range(rows_X)]
for i in range(rows_X):
    for j in range(cols_Y):
        for k in range(rows_Y):
            result[i][j] += X[i][k] * Y[k][j]
print(result)

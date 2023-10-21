def create_square_dict(n):
    square_dict = {}  
    for i in range(1, n + 1):
        square_dict[i] = i * i  
    return square_dict

n = int(input("Enter a value for n: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    result = create_square_dict(n)
    print("Dictionary containing (i, i*i) for i from 1 to", n, "is:")
    print(result)
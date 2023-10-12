def find_even_product_pairs(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    even_product_pairs = set()

    for num1 in even_numbers:
        for num2 in odd_numbers:
            even_product_pairs.add((num1, num2))
    
    for num in even_numbers:
        even_product_pairs.add((num, num))

    return even_product_pairs

# Example usage:
numbers = eval(input("ENTER A TUPLE: "))
result = find_even_product_pairs(numbers)
count =0
for pair in result:
    print(pair,end=" ")
    count +=1
print("\nTotal even pairs: ",count)

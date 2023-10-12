def sort_numbers(numbers):
    un, du = [], []
    for num in numbers:
        if num not in un:
            un.append(num)
        else:
            du.append(num)
            if num in un:
                un.remove(num)
    print("Tuple with unique elements: ",tuple(un))
    print("Tuple with duplicate elements: ",tuple(du))
 
 
# print the unique tuple by extracting all the unique elements
numbers = eval(input("ENTER A TUPLE: "))
sort_numbers(numbers)
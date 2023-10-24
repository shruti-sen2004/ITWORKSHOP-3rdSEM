numbers = [int(x) for x in eval(input("Enter a list of numbers: "))]

maximum_value = max(numbers, key=lambda x: x)


print(f"The maximum value in the list is: {maximum_value}")

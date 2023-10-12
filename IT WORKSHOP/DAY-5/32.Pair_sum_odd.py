numbers = eval(input("ENTER LIST: "))
odd_numbers = [x for x in numbers if x % 2 == 1]
result = []
for i in range(len(odd_numbers)):
    for j in range(i+1, len(odd_numbers)):
        result.append((odd_numbers[i], odd_numbers[j]))
print(f"The distinct pairs from the list {numbers} are: {result}")

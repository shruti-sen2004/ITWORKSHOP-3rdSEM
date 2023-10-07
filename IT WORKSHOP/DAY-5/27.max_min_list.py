numbers = eval(input("ENTER A LIST OF NUMBERS: "))
max = numbers[0]
min = numbers[0]
for num in numbers:
    # Check if num is greater than max
    if num > max:
        # Update max with num
        max = num
    # Check if num is less than min
    if num < min:
        # Update min with num
        min = num
print("The maximum value in the list is", max)
print("The minimum value in the list is", min)

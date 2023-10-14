try:
    number = float(input("Enter a number: "))
    if number >= 0:
        print("The number is:", number)
    else:
        raise ValueError("Entered number is negative!!")
except ValueError as e:
    print(e)

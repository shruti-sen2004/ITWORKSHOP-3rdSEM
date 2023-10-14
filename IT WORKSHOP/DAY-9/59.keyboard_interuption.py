try:
    number = int(input("Enter a number: "))
    square = number ** 2
    print("The square of", number, "is", square)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Ctrl + C was pressed.")

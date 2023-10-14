def get_valid_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    try:
        num1 = get_valid_number("Enter the first number: ")
        num2 = get_valid_number("Enter the second number: ")

        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            result = num1 * num2
            print("Result:", result)
        elif choice == '4':
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
    except Exception as e:
        print("An error occurred:", e)

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break

def decimal_to_binary(decimal_number) :
    binary = ""
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number //= 2
    return binary

def decimal_to_hexadecimal(decimal_number):
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal_number //= 16
    return hexadecimal

def decimal_to_octal(decimal_number):
    octal = ""
    while decimal_number > 0:
        octal = str(decimal_number % 8) + octal
        decimal_number //= 8
    return octal

def binary_to_decimal(binary_number):
    decimal = 0
    binary_number = str(binary_number)[::-1]  
    for i in range(len(binary_number)):
        if binary_number[i] == '1':
            decimal += 2**i
    return decimal

def binary_to_octal(binary_number):
    num= decimal_to_octal(binary_to_decimal(binary_number))
    return num

def binary_to_hexadecimal(binary_number): #not workimg properly
    num= decimal_to_hexadecimal(binary_to_decimal(binary_number))
    return num


def octal_to_binary(octal_number):
    binary_equiv = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }

    binary_number = ''
    for digit in octal_number:
        if digit in binary_equiv:
            binary_number += binary_equiv[digit]
        else:
            print("Invalid octal digit:", digit)
            return None

    return binary_number

def octal_to_decimal(octal_number):       
    num =binary_to_decimal(octal_to_binary(octal_number))
    return num

def octal_to_hexadecimal(octal_number):   
    num =binary_to_hexadecimal(octal_to_binary(octal_number))
    return num


def hexadecimal_to_binary(hexadecimal_number): 
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    binary_number = ''
    hexadecimal_number = hexadecimal_number.upper()  

    for digit in hexadecimal_number:
        if digit in hex_to_bin:
            binary_number += hex_to_bin[digit]
        else:
            return "Invalid hexadecimal digit"

    return binary_number

def hexadecimal_to_decimal (hexadecimal_number):
    num = binary_to_decimal(hexadecimal_to_binary(hexadecimal_number))
    return num
    
def hexadecimal_to_octal (hexadecimal_number):
    num = binary_to_octal(hexadecimal_to_binary(hexadecimal_number))
    return num

while True:
    print("Number Base Converter Menu:")
    print("1. Convert Decimal to Binary")
    print("2. Convert Decimal to Octal")
    print("3. Convert Decimal to Hexadecimal")
    print("4. Convert Binary to Decimal")
    print("5. Convert Binary to Octal")
    print("6. Convert Binary to Hexadecimal")
    print("7. Convert Octal to Binary")
    print("8. Convert Octal to Decimal")
    print("9. Convert Octal to Hexadecimal")
    print("10. Convert Hexadecimal to Binary")
    print("11. Convert Hexadecimal to Decimal")
    print("12. Convert Hexadecimal to Octal")
    print("13. Exit\n")
    
    choice = int(input("Enter your choice: "))

    if choice == 13:
        print("Goodbye!")
        break

    if choice in range(1,13):
        number = input("Enter the number: ")

        if choice == 1:
            result = decimal_to_binary(int(number))
            print(f"Binary: {result}\n")
        elif choice == 2:
            result = decimal_to_octal(int(number))
            print(f"Octal: {result}\n")
        elif choice == 3:
            result = decimal_to_hexadecimal(int(number))
            print(f"Hexadecimal: {result}\n")
        elif choice == 4:
            result = binary_to_decimal(int(number))
            print(f"Decimal: {result}\n")
        elif choice == 5:
            result = binary_to_octal(int(number))
            print(f"Octal: {result}\n")
        elif choice == 6:
            result = binary_to_hexadecimal(number)
            print(f"Hexadecimal: {result}\n")
        elif choice == 7:
            result = octal_to_binary(number)
            print(f"Binary: {result}\n")
        elif choice == 8:
            result = octal_to_decimal(number)
            print(f"Decimal: {result}\n")
        elif choice == 9:
            result = octal_to_hexadecimal(number)
            print(f"Hexadecimal: {result}\n")
        elif choice == 10:
            result = hexadecimal_to_binary(number)
            print(f"Binary: {result}\n")
        elif choice == 11:
            result = hexadecimal_to_decimal(number)
            print(f"Decimal: {result}\n")
        elif choice == 12:
            result = hexadecimal_to_octal(number)
            print(f"Octal: {result}\n")
    else:
        print("Invalid choice. Please select a valid option.\n")
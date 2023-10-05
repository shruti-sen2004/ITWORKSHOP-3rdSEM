string = input("Enter a string: ")
last_char = string[-1]
new_string = (string.replace(last_char, '*'))[0:len(string)-1] + last_char
print(f"New string: {new_string}")

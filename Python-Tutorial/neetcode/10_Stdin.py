user_input = input("Enter some text: ")
print(type(user_input), user_input)

age = int(input("Enter age: ")) # tupe conversion
print(type(age), age)

number_string = "1,2,3"
string_list = number_string.split(",")  # parsing input
print(string_list)

def add_two_numbers()-> int:
    line = input()
    num_list= line.split(",")
    return int(num_list[0])+int(num_list[1])
print(add_two_numbers())
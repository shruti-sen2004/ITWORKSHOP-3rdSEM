is_even = lambda x: x % 2 == 0

numbers = [int(x) for x in eval(input("Enter a list of numbers: "))]


even_list=[]
for number in numbers:
    if is_even(number):
        even_list.append(number)

print(f'List with even numbers is: {even_list}')


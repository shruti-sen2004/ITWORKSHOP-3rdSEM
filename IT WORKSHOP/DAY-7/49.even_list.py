num = eval(input("ENTER A LIST FOR NUMBERS: "))
is_even = lambda x: x%2==0

even_list=[]
for i in range(len(num)):
    if is_even(num[i]):
        even_list.append(num[i])
print("LIST WITH EVEN NUMBERS= ",even_list)

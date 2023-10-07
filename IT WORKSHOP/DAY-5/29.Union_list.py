list1 = eval(input("ENTER FIRST LIST: "))
list2 = eval(input("ENTER SECOND LIST: "))

for x in list2:
    if x not in list1:
        list1.append(x)
print("Union of the lists is:", list1)

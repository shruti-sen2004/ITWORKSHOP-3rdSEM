list1 = eval(input("ENTER FIRST LIST: "))
list2 = eval(input("ENTER SECOND LIST: "))
result = [x for x in list2 if x not in list1]
print(f"The numbers present in {list2} but not in {list1} are: {result}")

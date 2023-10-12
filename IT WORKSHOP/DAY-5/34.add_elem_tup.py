def summation(test_tup):
    test = list(test_tup)
    count = 0
 
    for i in test:
        count += i
    return count
 
 

test_tup = eval(input("ENTER A TUPLE: "))
print(summation(test_tup))
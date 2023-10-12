def mean(test_tup):
    test = list(test_tup)
    length= len(test)
    count = 0
 
    for i in test:
        count += i
    return count/length
 
 

test_tup = eval(input("ENTER A TUPLE: "))
print(mean(test_tup))


test_tup = eval(input("ENTER A TUPLE: "))
 

print("The original tuple is : " + str(test_tup))
 
res = dict()
x=list(test_tup)
y=[]
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    res[i]=x.count(i)
print("Tuple elements frequency is : " + str(res))
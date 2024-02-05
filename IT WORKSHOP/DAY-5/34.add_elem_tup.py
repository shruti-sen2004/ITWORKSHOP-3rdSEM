tup = eval(input("ENTER A TUPLE: "))
n= int(input("ENTER THE NUMBER OF TERMS YOU WANT TO ADD IN THE TUPLE: "))
for i in range(n):
    num= int(input("ENTER THE NUMBER YOU WOULD LIKE TO ADD: "))
    tup = tup + (num,)

print("NEW TUPLE: ",tup)

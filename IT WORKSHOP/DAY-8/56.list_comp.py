import random
l= int(input("ENTER A LOWER RANGE: "))
u =int(input("ENTER A UPPER RANGE: "))
n= int(input("ENTER THE NUMBER OF TERMS: "))
res = [random.randint(l,u) for i in range(n)]
print ("Random number list is : ",res)

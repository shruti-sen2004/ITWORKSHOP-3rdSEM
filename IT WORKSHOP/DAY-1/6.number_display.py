n= int(input("ENTER A NUMBER: "))

for i in range(4,0,-1):
   
    n= n%(10**i)
    print(n)

n= (input("ENTER A NUMBER: "))
#M-1
for i in range(4,0,-1):
    n= n%(10**i)
    print(n)

#M-2
for i in range(len(n),0,-1):
    print(n[:i:])

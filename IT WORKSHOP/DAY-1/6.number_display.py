n= input("ENTER A NUMBER: ")
#M-1
m= int(n)
for i in range(4,0,-1):
    m= m%(10**i)
    print(m)

#M-2
print("\n")
for i in range(len(n)):
    print(n[i::])

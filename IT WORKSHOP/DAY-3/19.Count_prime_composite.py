prime =0
composite =0
while(True):
    n = int(input("ENTER NO:(-1 to exit): "))
    if(n == -1):
        break
    else:
        c=0
        for i in range(1, n+1):
            if(n%i)==0:
                c +=1
                if c>2:
                    composite +=1
                    break
        if c ==2:
            prime +=1
print("NO. OF PRIME NUMBERS: ",prime)
print("NO. OF COMPOSITE NUMBERS: ",composite)
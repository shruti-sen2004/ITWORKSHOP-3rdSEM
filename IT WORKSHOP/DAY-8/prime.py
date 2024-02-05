def prime_or_not(num):
    f =0 
    i=1
    while i<=num:
        if num%i ==0:
            f +=1
        i +=1
    if f==2:
        return True
    else: 
        return False

def prime_range(a,b):
    for i in range(a,b+1):
        if prime_or_not(i)== True:
            print(i,end=" ")

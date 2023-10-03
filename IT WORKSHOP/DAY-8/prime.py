def prime_or_not(num):
    count =0
    i=1
    print("Factors are: ",end=" ")
    while i<=num:
        if num%i ==0:
            print(i,end=" ")
            count +=1
        i +=1
    if count ==2:
            print("\nNumber is prime")
    else: 
            print("\nNumber is not prime")

def prime_range(a,b):
    print("Prime numbers bertween",a,"and",b,"are: ",end=" ")
    for num in range(a,b+1):
        i=2
        for i in range(2,num):
            if(int(num % i)==0):
                i= num
                break;
        if i is not num:
            print(num, end=" ")

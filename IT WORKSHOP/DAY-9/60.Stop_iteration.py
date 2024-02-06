import random
count =0

l= int(input("ENTER THE LOWER BOUND= "))
u= int(input("ENTER THE UPPER BOUND= "))
print("RANDOM NUMBERS ARE: ",end=" ")
try:
    while True:
        if count>=10:
            raise ValueError("\n10 NUMBERS HAS BEEN DISPLAYED!!")
        
        num = random.randint(l,u+1)
        print(num,end=" ")
        count +=1
except ValueError as e:
    print(e)

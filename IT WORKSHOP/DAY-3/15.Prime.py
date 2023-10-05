num = int(input("ENTER THE NUMBER: "))
fact = 0
i =1
print("FACTORS ARE= ", end=" ")
while i<= num:
    if num %i ==0:
        print(i,end=" ")
        fact +=1
    i +=1
if fact ==2:
    print("\nIT IS A PRIME NUMBER!!")
else:
    print("\nIT IS NOT A PRIME NUMBER")
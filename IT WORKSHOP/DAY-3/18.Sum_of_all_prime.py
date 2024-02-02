l_num= int(input("ENTER the END NUMBER: "))
sum =0
for num in range(0,l_num+1):
    i=1
    for i in range(2,num):
        if(int(num%i)==0):
            i=num
            break
    if i is not num:
        sum += num
print("\nTHE SUM OF ALL PRIME NUMBERS: ",sum)

last_num = int(input("ENETR THE RANGE: "))
sum =0
for num in range(2, last_num +1):
    i =2
    for i in range(2, num):
        if(int(num % i)==0):
            i = num 
            break;
    if i is not num:
        sum += num
print("\nTHE SUM OF ALL PRIME NUMBERS: ",sum)
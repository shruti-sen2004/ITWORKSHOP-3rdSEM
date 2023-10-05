num = int(input("ENETR THE NUMBER: "))
sum =0
if num >=100 and num <=999:
    s = num
    while s>0:
        digit = s%10
        sum += digit **3
        s =s//10
if sum == num:
    print("IT IS A ARMSTRONG NUMBER!!")
else:
    print("IT IS NOT A ARMSTRONG NUMBER")
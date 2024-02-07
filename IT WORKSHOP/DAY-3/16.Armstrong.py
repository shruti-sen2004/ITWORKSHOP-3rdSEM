num = int(input("ENTER A NUMBER: "))
sum =0
o= len(str(num))

s= num
while s>0:
    digit = s%10
    sum += digit**o
    s= s//10

if sum == num:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")

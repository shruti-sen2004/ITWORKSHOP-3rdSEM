def lcm(x,y):
    if x>y:
        greater =x
    else:
        greater = y

    while(True):
        if((greater %x ==0)and (greater %y ==0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("ENTER ONE NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))
print("LCM :",lcm(num1, num2))

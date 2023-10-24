def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
def lcm(a,b):
    return (a * b)// gcd(a,b)


num_1 = int(input("ENTER THE FIRST NUMBER: "))
num_2 = int(input("ENTER THE SECOND NUMBER: "))

print("\nPRESS 1 TO FIND THE GCD OF TWO NUMBERS\nPRESS 2 TO FIND THE LCD OF TWO NUMBERS")
choice= int(input("\nENTER CHOICE: "))
if choice ==1: 
    print(f'\nThe GCD OF {num_1} AND {num_2} is {gcd(num_1,num_2)}')
elif choice ==2:
    print(f'\nThe LCM OF {num_1} AND {num_2} is {lcm(num_1,num_2)}')
else:
    print("\nINVALID CHOICE!!")
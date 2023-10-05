a = int(input("ENTER FIRST NUMBER: "))
b = int(input("ENTER SECOND NUMBER: "))
c = int(input("ENTER THIRD NUMBER: "))

if a>b and a>c:
    print(a,"is the largest number.")
    if b>c:
        print(b,"is the second largest number.")
        print(c,"is the smallest number.")
    else: 
        print(c,"is the second largest number.")
        print(b,"is the smallest number.")

if b>a and b>c:
    print(b,"is the largest number.")
    if a>c:
        print(a,"is the second largest number.")
        print(c,"is the smallest number.")
    else: 
        print(c,"is the second largest number.")
        print(a,"is the smallest number.")

if c>b and c>a:
    print(c,"is the largest number.")
    if b>a:
        print(b,"is the second largest number.")
        print(a,"is the smallest number.")
    else: 
        print(a,"is the second largest number.")
        print(b,"is the smallest number.")
a = int(input("ENTER START NUMBER: "))
b = int(input("ENTER END NUMBER: "))
print("THE DECIMAL EQUIVALENT FROM 1 /",a,"to 1 /",b,"is :")
for i in range(a,b+1):
    div = 1/i
    print("1 /",i,"=",div)
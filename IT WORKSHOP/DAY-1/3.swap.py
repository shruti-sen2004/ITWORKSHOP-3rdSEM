a= int(input("ENTER ONE NUMBER: "))
b= int(input("ENTER SECOND NUMBER: "))
print("ORIGINAL NUMBERS ARE",a,"AND",b)
#SWAP WITH THIRD VARIABLE
z=a
a=b
b=z
print("SWAPPED NUMBERS ARE",a,"AND",b)

#SWAP WITHOUT THIRD VARIABLE
a=a+b
b=a-b
a=a-b
print("SWAPPED NUMBERS ARE",a,"AND",b)
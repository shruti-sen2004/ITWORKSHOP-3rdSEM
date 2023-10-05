p = int(input("ENTER THE PRINCIPAL AMOUNT: "))
t = int(input("ENTER THE TIME: "))
if p< 200000:
    simp_int= (p*10*t)/100
elif 200000 <p <1000000:
    simp_int = (p*t*12)/100
else: 
    simp_int= (p*t*15)/100
print("SIMPLE INTEREST= ",simp_int)
n= int(input("HOW MANY PLAYERS WOULD YOU LIKE TO ENTER?? "))
dict={}
print('\n')

for i in range(0,n):
    name = input("ENTER PLAYERS NAME: ").capitalize()
    runs = int(input("ENTER THE RUNS: "))
    dict[name] = runs

print(dict)   

print("\nSEARCH THE PLAYER!!!")
search= input("ENTER THE PLAYERS NAME: ").capitalize()
if search in dict:
    print(f'{search} : {dict[search]}')
else:
    print(-1)
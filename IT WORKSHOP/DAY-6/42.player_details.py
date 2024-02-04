n= int(input("ENTER THE NUMBER OF PLAYERS THAT YOU WANT TO ENTER? "))
cricket ={}

for i in range(0,n):
    p_name = input("ENTER PLAYER NAME: ")
    p_sc= int(input("ENTER SCORE: "))
    cricket[p_name]= p_sc

print("\nSEARCH FOR THE PLAYER!!")

choice= "yes"
while choice.lower()=="yes":
    search = input("ENTER THE PLAYES YOU'RE SEARCHING: ")
    if search in cricket:
        print("SCORE: ",cricket[search])
    else:
        print(-1)
    choice= input("DO YOU WANT TO SEARCH FOR MORE PLAYERS? ")

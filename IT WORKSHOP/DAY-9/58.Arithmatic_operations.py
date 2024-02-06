choice = "yes"

while choice.lower()=="yes":
    try:
        n1= int(input("ENTER FIRST NUMBER: "))
        n2= int(input("ENTER SECOND NUMBER: "))

        print('''SELECT OPERATION:
                1. ADD
                2. SUBSTRACTION
                3. MULTIPLICATION
                4. DIVISION ''')
        ch= int(input("ENTER YOUR CHOICE: "))
        if ch in [1,2,3,4]:
            if ch==1:
                result = n1+n2
                print("RESULT: ",result)
            elif ch==2:
                result = n1-n2
                print("RESULT: ",result)
            elif ch==3:
                result = n1*n2
                print("RESULT: ",result)
            elif ch==4:
                if n2==0:
                    raise ValueError("DIVISION BY ZERO IS NOT POSSIBLE!!")
                else:
                    result = n1/n2
                    print("RESULT: ",result)
            else:
                raise ValueError("ENTER CORRECT CHOICE!!")
    except ValueError as e:
        print(e)
    choice= input("DO YOU WANT TO DO OTHER OPERATIONS?")

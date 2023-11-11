f_name = input("ENTER A FILE NAME: ")

with open(f_name,'r') as file:
    content = file.read()[::-1]
    print("CONTENT OF THE FILE IN REVERSE ORDER: ",content)
    with open('new.txt','w') as file:
        write= file.write(content)
        print("CONTENT IS COPIED!!")
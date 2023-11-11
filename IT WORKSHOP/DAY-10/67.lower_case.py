f_name = input('ENTER THE FILE NAME: ')

with open(f_name,'r') as file:
    content = file.read()
    with open('new_file_name.txt','w') as file:
        write = file.write(content.upper())
        print("Content is copied !!")
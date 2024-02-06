f_name= input("ENTER THE NAME OF THE FILE: ")

with open(f_name,'r') as file:
    content = file.readlines()
    with open('new_script.py','w') as file:
        for i in range(0,len(content)):
            if content[i][0]!="#":
                file.write(content[i])

print("CONTENT COPIED!!")

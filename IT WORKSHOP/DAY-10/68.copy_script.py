f_name= input("ENTER THE FILE NAME: ")
d_name= input("ENTER THE FILE NAME WHERE YOU WANT TO COPY THE FILE: ")

with open(f_name,'r') as source :
    with open(d_name,'w') as new_file:
        for line in source:
            if not line.lstrip().startswith('#'):
                new_file.write(line)
print("CONTENT COPIED!!")
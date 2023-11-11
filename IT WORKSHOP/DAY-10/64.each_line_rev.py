f_name = input("ENTER A FILE NAME: ")

with open(f_name, 'r') as file:
    content = file.readlines()
    print(f"\nEach line of {f_name} in reverse order: ")
    for i in content:
        print(i[::-1])
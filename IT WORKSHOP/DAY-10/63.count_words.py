f_name = input("ENTER THE FILE NAME: ")

with open(f_name, 'r') as file:
    content = file.read().split()
    word_count = len(content)
    print("TOTAL WORDS PRESENT: ",word_count)
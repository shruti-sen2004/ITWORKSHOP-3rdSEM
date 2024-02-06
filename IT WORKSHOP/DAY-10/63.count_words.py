f_name = input("ENTER THE FILE NAME: ")

with open(f_name,'r') as file:
    content = file.read().split()
    print(content)
    word_count = 0
    for ch in content:
        if ch.isalpha():
            word_count +=1
    print("TOTAL WORDS: ",word_count)

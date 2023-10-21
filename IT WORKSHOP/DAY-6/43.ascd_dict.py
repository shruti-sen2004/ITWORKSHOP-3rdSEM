def get_key(val):
   
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

my_dict = {"Java": 100, "Python": 112, "C": 11}

key_sort= sorted(my_dict.values())
for i in key_sort:
    print(f'{get_key(i)}: {i}')
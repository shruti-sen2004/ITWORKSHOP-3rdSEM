def merge_dict(dict1,dict2):
    merge_dict = dict1.copy()
    merge_dict.update(dict2)
    return merge_dict

d1= eval(input("ENTER A DICTIONARY: "))
d2= eval(input("ENTER ANOTHER DICTIONARY: "))
print("MERGED DICT= ",merge_dict(d1,d2))

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)  
    return merged_dict


dict1 = eval(input("ENTER THE FIRST DICTIONARY: "))
dict2 = eval(input("ENTER THE SECOND DICTIONARY: "))

merged_dict = merge_dicts(dict1, dict2)

print("Merged dictionary:")
print(merged_dict)

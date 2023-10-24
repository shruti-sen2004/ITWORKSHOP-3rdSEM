def upper_case(s):
    s_list = list(s)
    upper_count =0
    for i in range(0, len(s_list)):
        if s_list[i].isupper():
            upper_count += 1
    return upper_count
def lower_case(s):
    s_list = list(s)
    lower_count =0
    for i in range(0, len(s_list)):
        if s_list[i].islower():
            lower_count += 1
    return lower_count

str = input("ENTER A STRING: ")
print(f'The string: {str} has {upper_case(str)} upper case letters and {lower_case(str)} lower case letters.')

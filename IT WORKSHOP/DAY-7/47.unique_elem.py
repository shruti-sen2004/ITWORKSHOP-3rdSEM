def find_unique_elements(input_list):
    unique_elements = []
    
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
    
    return unique_elements


input_list = eval(input("ENTER A LIST: "))
unique_elements = find_unique_elements(input_list)
print("UNIQUE ELEMENTS OF THE LIST ARE:", unique_elements)
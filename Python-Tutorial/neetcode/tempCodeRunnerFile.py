def common_elements(list1, list2):
    return list(set(list1) & set(list2)) # intersection-> & , union-> |, difference-> -
print(common_elements([1,2,3,4],[6,4,7,3,5]))
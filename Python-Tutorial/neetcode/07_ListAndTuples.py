from typing import List
from collections import Counter

# List - Collection of items that are in a specific order
# it is similar to string
# Mutable - Value of the items stored can be changed
my_list = [1,7,5,4]
print(my_list[2]) # prints the third index
print(len(my_list))

my_list[0]= 100
print(my_list)

if 5 in my_list:
    print("5 is in my list") # this prints when 5 surely exists
else:
    print("5 is not in my list")
print() 

for element in my_list:
    print(element)
print()

def count_x(nums: List[int], x:int)-> int: # type annotation
    result = 0
    for n in nums:
        if n==x:
           result +=1 
    return result
print(count_x([1,2,5,6,5],5))

def count_x_v2(nums:List[int], x:int)-> int:
    count = Counter(nums) # using counter directory
    return count[x]

my_list.append(12) # this a method; both str and list ar objects in py
my_list.insert(2,"Avi")
print(my_list)

my_list.pop() # removes the last element by default
my_list.pop(0) # removes element at index 0
print(my_list)

print(my_list.index(5)) # index of first occurance

new_list= [1,7,5,8,9,6]
print(my_list[1:3]) # slicing


# Tuples - similar to lists but immutable like str
# ordered list of element
# indexing is possible 
my_tup = (1,2,3,)
print(my_tup[1])
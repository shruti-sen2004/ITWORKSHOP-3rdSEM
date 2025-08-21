from typing import List
from collections import Counter

# List - Collection of items that are in a specific order
# it is similar to string
# Arrays are called lists in python
# Mutable - Value of the items stored can be changed
my_list = [1,7,5,4]
print(my_list[2]) # prints the third index
print(len(my_list))

my_list[0]= 100 # constant time operation

if 5 in my_list:
    print("5 is in my list") # this prints when 5 surely exists
else:
    print("5 is not in my list")
print() 

# without index looping
for element in my_list:
    print(element)
print()

#with index and value
for i,n in enumerate(my_list):
    print(i,n)
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

# can be used as a stack
my_list.append(12) # this a method; both str and list ar objects in python

# not stack but array, insertion in middle is allowed 
# O(n) time operation
my_list.insert(2,"Avi") 

my_list.pop() # removes the last element by default
my_list.pop(0) # removes element at index 0

print(my_list.index(5)) # index of first occurance

new_list= [1,7,5,8,9,6]
print(my_list[1:3]) # slicing; end non inclusive

# array of size n with default values as 1
arr =[1]*5 # output : [1,1,1,1,1]

#unpacking
a,b,c = [1,2,3] # nos. variable lhs = nos.elements rhs

nums1 = [1,2,3] # loop through multiple arr simultaneously
nums2 = [4,5,6]
for n1,n2 in zip(nums1,nums2): # zip -combines arr of pairs
    print(n1,n2)
print()

arr = [1,5,10,3,8,22,4]
arr.reverse() # reverse the list
arr.sort() # sort in ascending; for string list arrange alphabeticaly
arr.sort(reverse="True") # sort in descending

# custom sort by length
arr =["bob", "shruti","alice","doe"]
arr.sort(key=lambda x:len(x))

arr =[i for i in range(5)] # list conprehension short hand

# 2-D list
arr =[[0]*4 for i in range(4)]
arr = [[0]*4]*4 # doesn't work properly- makes duplicate of 1 row rather creating 4 unique ones

# Tuples - similar to lists but immutable like str
# ordered list of element
# indexing is possible 
my_tup = (1,2,3,)
print(my_tup[1])

#maybe used as a key for hash map/set
myMap = {(1,2):3}
print(myMap[(1,2)])

myMap[[3,4]] = 5 # this is not possible
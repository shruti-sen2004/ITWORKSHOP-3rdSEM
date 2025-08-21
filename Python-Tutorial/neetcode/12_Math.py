print(5/2) # decimal division by default
print(5//2) # float division

print(-3//2) # rounds down in python; (floor) that is away from 0
# CAUTION: MOST PROGRAMMING LANGUAGE WILL ROUND UP; TOWARDS 0

print(int(-3/2)) # to get matching result as other languages

print(-10 % 3) # gives 2; not consistent with other langs

import math
print(math.fmod(10,-3)) # gives consistent result

print(math.floor(3/2)) # rounds down
print(math.ceil(3/2)) # round up
print(math.sqrt(4)) # square root
print(math.cbrt(8)) # cube root
print(math.pow(2,5)) # to the power

# Max / Min Int - Infinity so they never overflow
float("inf")
float("-inf")

# use inbuit sum(), min() and max()
def find_sum(nums):
    return sum(nums)
print(find_sum([1,2]))
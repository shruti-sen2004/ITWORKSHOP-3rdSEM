import random
nums=[]
l = int(input("ENTER THE LOWER RANGE: "))
u = int(input("ENTER THE UPPER RANGE: "))
n = int(input("ENTER THE NUMBER OF TERMS: "))
for i in range(n):
    nums.append(random.randint(l,u))
print("The original list is: ",nums)
random.shuffle(nums)
print("The shuffled list is: ",nums)
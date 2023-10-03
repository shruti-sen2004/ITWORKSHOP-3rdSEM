import random,math
nums= []
l= int(input("ENTER THE LOWER RANGE: "))
u= int(input("ENTER THE UPPER RANGE: "))
n= int(input("ENTER THE NUMBER OF TERMS: "))
sum =0
for i in range(n):
    num = random.randint(l,u)
    sum += num
    nums.append(num)
nums.sort()
print("List: ",nums)

#MEAN
mean = sum/n
print("MEAN: ",mean)

#MEDIAN
if n%2 !=0:
    mid =n//2
    print("MEDIAN: ",nums[mid])
else:
    mid= n//2
    print("MEDIAN: ",(nums[mid]+nums[mid+1])/2)

#SD
sum_sd =0
for i in range(n):
    sum_sd += (nums[i] -mean)**2
sd= round(math.sqrt(sum_sd/n),4)
print("Standard Deviation: ",sd)
# while loop
# also don't declare a new scope
i=0
while i < 10 : # counting 0 to 9
    print(i)
    i += 1
print()

n=10
while n < 100 : # printing multiples of 10 upto 90
    print(n)
    n += 10
print()

# for-loop
for i in range(10): # 0 to 9
    print(i)
print()

for i in range(2,55,2): # start, stop before, step(can be + or -)
    print(i)
print()

for i in reversed(range(10,21)): # for reverse printing we can also use this
    print(i)
print()

# Nested-loop
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
print()

# Control flow
if True:
    pass # acts as a placeholder for empty functions

for i in range(1,8):
    if i == 3:
        continue # breaks further compilation and just moves to next iteration
    elif i == 6:
        break # completly terminates the execution
    print(i)
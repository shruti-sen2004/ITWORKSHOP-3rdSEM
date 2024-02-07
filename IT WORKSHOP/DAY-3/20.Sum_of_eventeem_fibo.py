def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

s = 0
l = int(input("ENTER THE ENDING RANGE: "))
for i in range(l+1):
    if (fib(i) > l):
        break
    else:
        if (fib(i) % 2 == 0):
            print(fib(i))
            s += fib(i)

print('Sum of even terms is:', s)

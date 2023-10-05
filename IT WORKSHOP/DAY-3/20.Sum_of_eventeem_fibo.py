def fibo_even_sum(limit):
    a,b = 1,2
    even_sum = 0
    while b<= limit:
        if b % 2==0:
            even_sum += b
        a,b = b, a+b
    return even_sum

limit =100
result = fibo_even_sum(limit)
print("SUM of even terms of fibonacchi series upto 100 is: ",result)

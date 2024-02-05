#M-1
num = eval(input("ENTER A TUPLE: "))
even =[n for n in num if n%2==0]
odd= [n for n in num if n%2!=0]
print(even, odd)
even_pairs= set()
for i in even:
    for j in odd:
        even_pairs.add((i,j))
for k in even:
    even_pairs.add((k,k))

print(even_pairs)

#M-2
numbers = eval(input("ENTER A TUPLE: "))
pairs = [] 
for i in range(len(numbers)): 
    for j in range(i+1, len(numbers)): 
      if (numbers[i] * numbers[j]) % 2 == 0: 
        pairs.append((numbers[i], numbers[j])) 
print("The pairs are:", pairs)

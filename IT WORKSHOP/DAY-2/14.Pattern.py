'''
1
2 3
4 5 6 
7 8 9 10
11 12 13 14 15 
'''

n = int(input("ENTER THE NUMBER OF ROWS: "))
num =1
for i in range(0,n):
    for j in range(0,i+1):
        print(num, end=" ")
        num += 1
    print()

'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n = int(input("\n\n\nENTER THE NUMBER OF ROWS: "))
for a in range(n,0,-1):
    for b in range(n -a):
        print(' ',end=' ')
    for b in range(2*a-1):
        print('*',end =' ')
    print()
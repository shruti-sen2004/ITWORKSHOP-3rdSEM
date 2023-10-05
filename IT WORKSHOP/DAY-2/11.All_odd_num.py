start = int(input("ENTER THE START RANGE: "))
end= int(input("ENTER THE END RANGE: "))
print("ODD NUMBERS BETWEEN ",start,"AND",end,"ARE: ", end=" ")
while(start<end):
    if(start%2 !=0):
        print(start, end=" ")
    start += 1
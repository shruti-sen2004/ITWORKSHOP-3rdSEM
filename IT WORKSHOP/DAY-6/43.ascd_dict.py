my_dict = eval(input("ENTER A DICTIONARY: "))

val_sorted= sorted(my_dict.values())
# val_sorted= list(my_dict.values())
# for i in range(len(val_sorted)):
#     for j in range(i + 1, len(val_sorted)):
#         if val_sorted[i] > val_sorted[j]:
#            val_sorted[i], val_sorted[j] = val_sorted[j], val_sorted[i]

new_dict={}
for i in range(0,len(val_sorted)):
    for key,val in my_dict.items():
        if val_sorted[i]== val:
            new_dict[key]= val
print("SORTED DICTIONARY: ",new_dict)

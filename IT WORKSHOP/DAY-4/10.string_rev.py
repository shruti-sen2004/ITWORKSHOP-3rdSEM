s= input("ENTER A STRING: ")
s_new= s[::-1]

if s.lower()== s_new.lower():
    print("STRING IS PALINDROME")
else:
    print("STRING IS NOT PALINDROME")
def palindrome(s):
    s_new =s[::-1]
    if s_new.lower() == s.lower():
        print("PALINDROME")
    else:
        print("NOT PALINDROME")
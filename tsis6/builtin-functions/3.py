# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def palindrom(p):
    return p == p[::-1]

p = input()

if palindrom(p):
    print("True")
else:
    print("False")


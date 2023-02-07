# Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def palindrome(a):
    for x in range(int(len(a)/2)):
        if a[x] != a[len(a)-x-1]:
            return False
    return True

a = str(input())
if palindrome(a):
    print("Yes")
else:
    print("No")
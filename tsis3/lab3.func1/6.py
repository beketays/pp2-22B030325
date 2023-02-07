# Write a function that accepts string from user, return a sentence with the words reversed.
# We are ready -> ready are We

def reverse(s):
    for x in s[::-1]:
        print (x, end = " ")


l = [ x for x in input().split()]
reverse(l)
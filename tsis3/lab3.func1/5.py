# Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations  
def permut(st):
    p = permutations(st)
    for a in list(p):
        print(a)

ans = [x for x in input()]
permut(ans)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Note: don't use collection set.

def unique(l):
    d={}
    new_l=[]
    for x in l:
        d[x] = 1
    for x in d.keys():
        new_l.append(x)
    print(new_l)

list = [ str(x) for x in input().split()]
unique(list)
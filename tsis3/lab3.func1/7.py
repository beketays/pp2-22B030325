# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(i):
    for x in range(1, len(i)):
        if i[x]==3 and i[x-1]==3:
            return True
    return False

l= [int(x) for x in input().split()]

print(has_33(l))

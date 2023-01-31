thislist = ["orange", "mango", "apple", "cherry"]
thislist.sort()
print(thislist)


thislist = [100, 70, 30, 2]
thislist.sort()
print(thislist)


thislist = ["apple", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 23, 82]
thislist.sort(key = myfunc)
print(thislist)


# By default the sort() method is case sensitive,
# resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry", "Apple", "apple"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)








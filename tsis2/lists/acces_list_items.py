thislist = ["apple", "banana", "cherry"]
print(thislist[1])        # The first item has index 0.


thislist = ["apple", "banana", "cherry"]
print(thislist[-2])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        
# The search will start at index 2 (included) and end at index 5 (not included).   
# first item has index 0.


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# This will return the items from index 0 to index 4.
# index 0 is the first item, and index 4 is the fifth item
# the item in index 4 is NOT included


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# This will return the items from index 2 to the end.
# index 0 is the first item, and index 2 is the third


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])    # Negative indexing means starting from the end of the list.
# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1


thislist = ["apple", "banana", "cherry"]
if "apple" it thislist:
    print("Yes, 'apple' is in the fruits list")








fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# newlist = [expression for item in iterable if condition == True]



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)



newlist = [x for x in range(10)]
print(newlist)



newlist = [x for x in range(10) if x < 5]
print(newlist)



fruits = ["apple", "banana", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)



fruits = ["apple", "banana", "mango", "cherry"]
newlist = ['hello' for x in fruits]
print(newlist)



fruits = ["apple", "banana", "cherry", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)







fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Loop through the letters in the word "banana":
for x in "banana":
  print(x)


# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break


# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6):
  print(x)


# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)


# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")


#If the loop breaks, the else block is not executed.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


# having an empty for loop like this, would raise an error without the pass statement
for x in [0, 1, 2]:
  pass



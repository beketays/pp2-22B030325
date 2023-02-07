# Create a lambda function that takes one parameter (a) and returns it.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
def sqare(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())

for i in sqare(a, b):
    print(i)

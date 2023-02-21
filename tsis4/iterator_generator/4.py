def squar(x, y):
    for i in range(x, y+1):
        yield i*i

x = int(input())
y = int(input())

for num in squar(x, y):
    print(num)
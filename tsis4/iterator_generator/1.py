def gener(n):
    for i in range(n+1):
        yield i**2
for i in gener(int(input())):
    print(i)
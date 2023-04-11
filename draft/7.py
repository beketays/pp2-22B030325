def gen(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i

for i in gen(int(input())):
    print(i)
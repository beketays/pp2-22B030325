def gen(x):
    while x >= 0:
        yield x
        x -= 1

ans = gen(int(input()))
for i in ans:
    print(i)
def gener(x):
    while x >= 0:
        yield x
        x -= 1

for i in gener(int(input())):
    print(i)
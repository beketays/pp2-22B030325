def divis(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divis(int(input())):
    print(num)   
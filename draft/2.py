def even_num(n):
    for a in range(n+1):
        if a%2 == 0:
            yield a

n = int(input())
even = even_num(n)

for a in even:
    print(a, end=", ")

'''def even_num(n):
    for num in range(n+1):
        if num % 2 == 0:
            yield num

n = int(input())
even = even_num(n)

for num in even:
    print(num, end=", ")
    '''
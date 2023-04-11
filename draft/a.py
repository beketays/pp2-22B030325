def func(a):
    s = sorted([i for i in a if i!=-1])
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i]=s[j]
            j+=1
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]

print(func(a))


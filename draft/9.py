import math
def generator(n):
    i = 0
    while i > 0:
        if i % 5 == 0:
            yield i**0.5
            
n = int(input())
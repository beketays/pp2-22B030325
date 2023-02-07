'''You are given list of numbers separated by spaces.
Write a function filter_prime which will take list of numbers 
as an agrument and returns only prime numbers from the list. '''

def filter_prime(n):
    for x in range(2, int(n ** 0.5)+1):
        if n % x == 0:    
            return False     # not prime 
    return True        # prime

p = [int(x) for x in input().split()]
for x in p :
    if filter_prime(int(x)):
        print(x)

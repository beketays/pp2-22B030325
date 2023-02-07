'''Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
'''

def solve(numhead, numleg):     
    print("Number of rabbits:", (numleg - 2 * numhead) // 2)
    print("Number of chickens:", (numhead - (numleg - 2 * numhead) // 2))

# // - Floor division

numhead, numleg = map(int, input().split())     # input().split() - разделить строку на части по пробелам 
solve(numhead, numleg)

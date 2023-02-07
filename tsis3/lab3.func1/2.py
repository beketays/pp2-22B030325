'''Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)
'''
def temp(F):
    C = ((5 / 9) * (F - 32))
    print(C)

x = int(input())
temp(x)

print(int(3 ** 0.5))
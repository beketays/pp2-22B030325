# Write a Python program that invoke square root function after specific milliseconds.

import time
import math

a = int(input())
b = int(input())
time.sleep(b/1000)  #кнопка остановки

print("Square root of", a, " after", b, "miliseconds is", math.sqrt(a))
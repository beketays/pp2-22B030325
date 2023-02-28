# Write a Python program to convert a given camel case string to snake case.

import re

def func(word):
    return word.group("a")+ "_" + word.group("b").lower()

txt = "mySuperVar" 
x = "(?P<a>[a-z])(?P<b>[A-Z])+"

print(re.sub(x, func, txt))
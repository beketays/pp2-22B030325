# Write a Python program to find the sequences of one upper case letter followed by lower case letters.


import re

txt = "Almaty is the best City"

s = "[A-Z][a-z]"

x = re.findall(s, txt)
print(x)
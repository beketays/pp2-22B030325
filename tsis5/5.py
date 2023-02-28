# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re 

txt = "He was so tiredb"
s = 'a.*b$'

x = re.search(s, txt)

print(x) 
# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

txt = "kbtu abb abbb abbb aba abbd abc acd accc acddd"

s = r'a(bb|bbb)'

x = re.search(s, txt)
print(x)
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

txt = "bbtu ab aab abbb aaabbb"
s = r"ab*"
x = re.search(s, txt)
print(x)
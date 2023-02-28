# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

txt = "ala school a_b course "
s = "[a-z]_[a-z]"
x = re.findall(s, txt)
print(x)
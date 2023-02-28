# Write a Python program to split a string at uppercase letters.

import re

txt = "I have so many Opportunities"

x = re.split("[A-Z]", txt)
print(x)
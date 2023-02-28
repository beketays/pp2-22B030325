# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

txt = "today the weather was not bad"

s = "[ .,]"

x = re.sub(s, ":", txt)
print(x)
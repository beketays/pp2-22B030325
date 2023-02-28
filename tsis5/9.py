# Write a Python program to insert spaces between words starting with capital letters.

import re 

txt= "DoNotBeSilly"

s = r"([A-Z][a-z]+)"

x = re.sub(s, r" \1", txt).strip()
print(x)
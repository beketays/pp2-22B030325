import re

txt = "DFGtoday, was.  good day "

s = r"[,;.&?:!@#$%^&*()_+]"

a = txt.lower()
x = re.sub(s, "", txt)


c = re.sub(r'[ ]{2:}', ' ', txt)
print(a)
print(c)
print(x)
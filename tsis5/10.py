# Write a Python program to convert a given camel case string to snake case.

import re

txt = "PythonIsAPopularProgrammingLanguage"

x = r"(?<!^)(?=[A-Z])"
s = re.sub(x, '_', txt).lower()

print(s)
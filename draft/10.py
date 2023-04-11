import re
import os

text = open("/Users/symbat/Documents/pp2-22B030325/draft/data.txt", "r")
pattern = re.sub("[1-9][1-9][1-9]", "aaa", text.read())
print(pattern)
import re

text = open("/Users/symbat/Documents/pp2-22B030325/draft/data.txt", "r")
pattern = re.sub("ab", "cd", text.read())
print(pattern)
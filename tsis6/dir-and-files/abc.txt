# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = r"/Users/symbat/Documents/pp2-22B030325/tsis6"

print ("Only directories:")
x = []
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        x.append(name)
print(x)

print("\nOnly files:")
y = []
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        y.append(name)
print(y)

print("\nAll directories and files:")
z=[]
for name in os.listdir(path):
    z.append(name)
print(z)

"""
Only directories:
['builtin-functions', 'dir-and-files']

Only files:
['abc.txt', 'abc.py']

All directories and files:
['builtin-functions', 'abc.txt', 'dir-and-files', 'abc.py']
"""
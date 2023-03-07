# Write a Python program to test whether a given path exists or not. 
# If the path exist find the filename and directory portion of the given path.

import os 
print("Test a path exists or not:")
path = r"/Users/symbat/Documents/pp2-22B030325/tsis6/dir-and-files/2.py"
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))

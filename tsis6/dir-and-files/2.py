# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os

print('Exist:', os.access(r"/Users/symbat/Documents/pp2-22B030325/tsis6", os.F_OK))
print('Readable:', os.access(r"/Users/symbat/Documents/pp2-22B030325/tsis6", os.R_OK))
print('Writable:', os.access(r"/Users/symbat/Documents/pp2-22B030325/tsis6", os.W_OK))
print('Executable:', os.access(r"/Users/symbat/Documents/pp2-22B030325/tsis6", os.X_OK))

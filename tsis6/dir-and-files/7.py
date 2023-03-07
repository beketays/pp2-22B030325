# Write a Python program to copy the contents of a file to another file

import shutil

file = r"/Users/symbat/Documents/pp2-22B030325/tsis6/dir-and-files/1.py"
file1 = r"/Users/symbat/Documents/pp2-22B030325/tsis6/dir-and-files/abc.txt"
shutil.copy(file, file1)
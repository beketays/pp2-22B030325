# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os

if os.path.exists(r"/Users/symbat/Documents/pp2-22B030325/tsis6/abc.py"):
  os.remove(r"/Users/symbat/Documents/pp2-22B030325/tsis6/abc.py")
  
else:
  print("The file does not exist")
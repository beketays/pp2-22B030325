# Write a Python program to count the number of lines in a text file.

with open(r'/Users/symbat/Documents/pp2-22B030325/tsis6/dir-and-files/abc.txt', 'r') as file:
    lines = len(file.readlines())
    print('Total Number of lines:', lines)
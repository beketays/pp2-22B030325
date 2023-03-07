# Write a Python program to write a list to a file.

list = ['book', 'pen', 'bag']
path = r"/Users/symbat/Documents/pp2-22B030325/tsis6/dir-and-files/abc.txt"
with open(path, 'w') as f:
    for element in list:
        f.write(element + '\n')
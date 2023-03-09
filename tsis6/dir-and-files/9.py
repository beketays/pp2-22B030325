import os

path = r"/Users/symbat/Documents/pp2-22B030325/tsis6/dir-and-files/abc.txt"

def gener(path):
    with open(path, "r") as f:
        for line in f:
            yield line


print(next(gener(path)))

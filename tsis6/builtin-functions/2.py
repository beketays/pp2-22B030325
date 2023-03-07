# Write a Python program with builtin function that accepts a string and 
# calculate the number of upper case letters and lower case letters
import os  # current working directory / путь к текущей папке

file = open(r"/Users/symbat/Documents/pp2-22B030325/tsis6/abc.txt", "r")

def gen(file):
    with open(file, "r") as f:
        for element in f:
            yield element

iter(gen(file))

print(next(gen(file)))

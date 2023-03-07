# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string
import os

files = [f"{i}.txt" for i in string.ascii_uppercase]

for file in files:
    with open(file, "w"):
        pass
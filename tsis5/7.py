# Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(word):
    return ''.join(x.capitalize() for x in word.split('_'))

print(snake_to_camel('the_best'))
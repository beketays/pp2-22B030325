
import re
def func(word):
    return word.group("a")+ "_" + word.group("b").lower()
txt = "mySuperVar" 
x = "(?P<a>[a-z])(?P<b>[A-Z])+"
print(re.sub(x, func, txt))


"""
txt = "camelCaseString"
pattern = r"(?<!^)(?=[A-Z])"
snake = re.sub(pattern, '_', txt).lower()

print(snake)
"""
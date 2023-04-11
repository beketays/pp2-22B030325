# Define a class which has at least two methods: getString:
# to get a string from console input printString: to print the string in upper case.

class myclass:
    def getstring():
        pass
    def __init__(self, txt):
        self.txt=txt
    def printString(self):
        print(self.txt.upper())
        
p1=  myclass(input())
p1.printString()


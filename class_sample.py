"""

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""

class InputOutString:

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

    def testDef(self):
        print("This is test method")

instance = InputOutString()
instance.getString()
instance.printString()
instance.testDef()

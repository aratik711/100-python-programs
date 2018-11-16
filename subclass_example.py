"""

Question:
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.

"""


class American:

    def printnationality(self):
        print("America")


class NewYorker:

    def printcity(self):
        
        American.printnationality(self)
        print("New York")


citizen = NewYorker()
citizen.printcity()


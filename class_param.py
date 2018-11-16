"""

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later

"""

class Person:

    name = "Person"

    def __init__(self, name = None):
        self.name = name

john = Person("John")
print("Name of %s is %s" % (Person.name, john.name))

jane = Person()
jane.name = "Jane"
print("Name of %s is %s" % (Person.name, jane.name))
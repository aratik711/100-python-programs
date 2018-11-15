"""

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

"""
class generator:
    def putNumber(self, n):
        i = 0
        while i < n:
            j = i
            i = i + 1
            if j % 7 == 0:
                yield j

gen = generator()

for i in gen.putNumber(100):
    print("")
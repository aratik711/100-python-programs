"""

Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

"""


def even_or_odd(num):
    if num%2 == 0:
        print("It's an even number")
    else:
        print("It's an odd number")


num = int(input())
even_or_odd(num)
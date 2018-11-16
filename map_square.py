"""

Question:
Write a program which can use map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.

"""


my_list = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x: x**2, my_list))
print(square)

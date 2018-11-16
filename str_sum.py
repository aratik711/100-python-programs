"""

Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

"""


def my_sum(num1, num2):
    return int(num1)+int(num2)


num1, num2 = input().split(" ")
print(my_sum(num1, num2))
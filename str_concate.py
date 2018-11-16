"""

Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings

"""


def concat(str1 = "",str2 = ""):
    print(str1+""+str2)


str1, str2 = input().split(" ")
concat(str1, str2)

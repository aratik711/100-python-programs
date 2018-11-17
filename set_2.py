"""

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

"""


def unique(li):

    my_list = []
    seen = set()
    for x in li:
        if x not in seen:
            seen.add(x)
            my_list.append(x)
    return my_list


li = [12,24,35,24,88,120,155,88,120,155]
print(unique(li))


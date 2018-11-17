"""

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.

"""


import math
def bin_search(arr, num):

    bottom = 0
    top = len(arr)-1
    index = -1
    while (top >= bottom) and (index == -1):

        mid = int(math.floor((top+bottom)/2.0))
        if arr[mid] == num:
            index = mid
        elif arr[mid] > num:
            top = mid-1
        else:
            bottom = mid+1

    return index


li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))


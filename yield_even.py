"""

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

"""


def even(num):

    i = 0
    while i <= num:
        j = i
        i += 1
        if j%2 == 0:
            yield j


num = int(input())
values = []
for i in even(num):
    values.append(str(i))
print(",".join(values))



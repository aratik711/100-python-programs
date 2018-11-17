"""

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def divide(num):

    i = 0
    while i <= num:
        j = i
        i += 1
        if j%5 == 0 and j%7 == 0:
            yield j


num = int(input())
my_list = []
for i in divide(num):
    my_list.append(str(i))
print(",".join(my_list))

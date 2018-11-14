"""

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

cnt_upper, cnt_lower = 0, 0

line = input()

for char in line:
    if char.isupper():
        cnt_upper += 1
    if char.islower() :
        cnt_lower += 1
print("UPPER CASE  "+str(cnt_upper))
print("LOWER CASE " + str(cnt_lower))
"""

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

cnt_letter, cnt_digit =0,0

line = input()

for char in line:
    if char.isalpha():
        cnt_letter += 1
    if char.isdigit():
        cnt_digit += 1
print("LETTERS "+str(cnt_letter))
print("DIGITS " + str(cnt_digit))
"""

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

"""

num = int(input())

num1 = int("%s" % num)
num2 = int("%s%s" % (num, num))
num3 = int("%s%s%s" % (num, num, num))
num4 = int("%s%s%s%s" % (num, num, num, num))

print(num1+num2+num3+num4)

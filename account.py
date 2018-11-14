"""

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

total = 0

while True:
    transaction = input()
    if transaction:
        operation, amount = transaction.split(" ")
        if operation == "D":
            total += int(amount)
        if operation == "W":
            total -= int(amount)
    else:
        break

print(total)

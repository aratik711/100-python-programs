"""

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

"""

subject = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey","Football"]
for i in subject:
    for j in verb:
        for k in obj:
            print("%s %s %s" %(i, j, k))

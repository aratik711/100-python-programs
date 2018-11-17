"""

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.


"""

def solve(heads, legs):
    for i in range(heads+1):
        j = heads-i
        if 2*i+4*j==legs:
            return i,j
    return "No solution"


heads=35
legs=94
solutions=solve(heads,legs)
print(solutions)
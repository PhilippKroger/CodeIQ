"""

https://www.codewars.com/kata/554f76dca89983cc400000bb/train/python

"""


def sol_equa(n):
    # your code

    for i in range(100):
        for j in range(100):
            if (i**2) - (4 * (j**2)) == n:
                return [i, j]
            else:
                continue


# x2 - 4 * y2 = (x - 2*y) * (x + 2*y)
print(sol_equa(12))
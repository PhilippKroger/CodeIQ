
from random import randint

n = 5000

a = [randint(0, 1000) for i in range(n)]

#  simple enumeration of values
k = 0


def f_enum(a):
    global k
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % 3 == 0:
                k += 1
    return k


print(f_enum(a))







from random import randint

n = 5000

a = [randint(0, 1000) for i in range(n)]

#  simple enumeration of values
k = 0


def f_enum(a):
    global k
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] * a[j]) % 15 == 0 and (a[i] + a[j]) % 2 != 0:
                k += 1
    return k


print(f_enum(a))


#  find all divisors
all_divs = []


def f_div(number):
    global all_divs
    for i in range(1, number+1):
        if number % i == 0:
            all_divs.append(i)
    return all_divs


print(f_div(15))


k1, k3, k5, k15, s = 0, 0, 0, 0, 0
k2, k4, k6, k8, k9 = 0, 0, 0, 0, 0

def func(a):
    global k1, k3, k5, k15, s
    for x in a:
        if x % 15 == 0 and x % 2 != 0:
            s += k1 + k3 + k5 + k15
            k15 += 1
        elif x % 5 == 0 and x % 2 != 0:
            s += k3 + k15
            k5 += 1
        elif x % 3 == 0 and x % 2 != 0:
            s += k5 + k15
            k3 += 1
        else:
            s += k15
            k1 += 1
    return s


print(func(a))

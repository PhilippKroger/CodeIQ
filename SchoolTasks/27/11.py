
from random import randint

n = 5000

a = [randint(0, 1000) for i in range(n)]

#  simple enumeration of values
k = 0


def f_enum(a):
    global k
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] * a[j]) % 105 == 0:
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


print(f_div(105))


k1, k3, k5, k7, k15, k21, k35, k105, s = 0, 0, 0, 0, 0, 0, 0, 0, 0


def func(a):
    global k1, k3, k5, k7, k15, k21, k35, k105, s
    for x in a:
        if x % 105 == 0:
            s += k1 + k3 + k5 + k7 + k15 + k21 + k35 + k105
            k105 += 1
        elif x % 35 == 0:
            s += k3 + k15 + k21 + k105
            k35 += 1
        elif x % 21 == 0:
            s += k5 + k15 + k35 + k105
            k21 += 1
        elif x % 15 == 0:
            s += k7 + k21 + k35 + k105
            k15 += 1
        elif x % 7 == 0:
            s += k15 + k105
            k7 += 1
        elif x % 5 == 0:
            s += k21 + k105
            k5 += 1
        elif x % 3 == 0:
            s += k35 + k105
            k3 += 1
        else:
            s += k105
            k1 += 1
    return s


print(func(a))

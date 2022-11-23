from random import randint
from time import time


n = 50
a = [randint(0, 1000) for i in range(n)]
k1 = 0
k3 = 0
k7 = 0
k21 = 0
s = 0
for i in range(n):
    if a[i] % 21 == 0:
        s += (k1+k3+k7+k21)
        k1 += 1
        k3 += 1
        k7 += 1
        k21 += 1
    if a[i] % 7 == 0:
        s += (k1+k7+k21)
        k1 += 1
        k7 += 1
        k21 += 1
    if a[i] % 3 == 0:
        s += (k1+k3+k7)
        k1 += 1
        k3 += 1
    if a[i] % 1 == 0:
        s += (k1+k3+k7+k21)
        k1 += 1
        k3 += 1
        k7 += 1
        k21 += 1
print(s)

k = 0
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i]*a[j])%21==0:
            k += 1
print(k)
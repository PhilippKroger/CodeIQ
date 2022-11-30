from random import randint

n = 5000
a = [randint(0, 1000) for i in range(n)]
k = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] * a[j]) % 10 == 9:
            k += 1
print(k)

k9, k7, k3, k1, s = 0, 0, 0, 0, 0
for x in a:
    if x % 10 == 9:
        s += k1
        k9 += 1
    elif x % 10 == 7:
        s += k7
        k7 += 1
    elif x % 10 == 3:
        s += k3
        k3 += 1
    else:
        s += k9
        k1 += 1
print(s)

from math import log

a = 70
a = bin(a)[2:]
n = len(a)
k = 0
print(a)
while not (2 ** k > k + n):
    k += 1
m = n + k
b = [0] * (m + 1)


for i in range(1, len(b)):
    if log(i, 2) != int(log(i, 2)):
        b[i] = int(a[0])
        a = a[1:]
b = b[1:]
print(b)

rk = 2
for i in range(k):
    ki = 2**i
    s = 0
    j = i+1
    while j <=m:
        for j1 in range(i):
            if j + j1 <= 12:
                s += b[j + j1]
            else:
                break
        j += rk
    rk += 2
    print(s)
    if s % 2 == 1:
        s = 1
    else:
        s = 0
    b[2**i] = s
print(b)

"""
    for j in range(ki, m, 2*ki):
        print(j)

        for j1 in range(i):
            s += b[j+j1]
        """
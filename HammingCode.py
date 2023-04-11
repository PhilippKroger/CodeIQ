from math import log


def hamming_code(a):
    """Hamming Code Function"""
    n = len(a)
    k = 0
    while (2 ** k > k + n) == False:
        k += 1
    m = n + k
    b = [0] * (m + 1)
    for i in range(1, len(b)):
        if log(i, 2) != int(log(i, 2)):
            b[i] = int(a[0])
            a = a[1:]
    for i in range(k):
        x = 2
        ki = 2 ** i  # 1, 2, 4, 8
        s = 0
        j = ki
        while j <= m:  # ki < m
            if i > 0:
                for j1 in range(j):
                    if j + j1 < len(b):
                        s += b[j + j1]
            else:
                s += b[j]  # i == 1
            j += x ** (i + 1)  # 12 -> 13
        b[ki] = s % 2
    return b[1:]


a = bin(int(input()))[2:]
print(hamming_code(a))

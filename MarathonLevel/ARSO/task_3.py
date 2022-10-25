from math import sqrt
s = 0
n = int(input())
m = int(input())
if (1+n)*n//2<m:
    print(0)
else:
    s = 0
    k = int(sqrt(n**2 + n - 2 * m))
    while n != k:
        print(n)
        s += n
        n -= 1
    if m-s!=0:
        print(m-s)



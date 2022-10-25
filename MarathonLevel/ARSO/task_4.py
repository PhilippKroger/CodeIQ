n = int(input())
m = int(input())
km = n // 2
kn = n // 2
n1 = n
nk = n-2*(kn-1)
sn = n + (n1 + nk) * kn // 2
m1 = m - 2
mk = m - 2*km
sm = (m1+mk)*km//2
print(sn+sm)
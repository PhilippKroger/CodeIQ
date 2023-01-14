k = 0

for p in range(10000000, 99999999+1):
    p1 = p // 10000000
    p2 = p // 1000000 % 10
    p7 = p // 10 % 10
    p8 = p % 10
    if p1==p7 and p2==p8:
        k += 1
print(k)
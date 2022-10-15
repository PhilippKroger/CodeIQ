b, e = map(int, input().split())
k = 0
if b % 2 == 0 and e % 2 == 0:
    for i in range(b+1, e+1, 2):
        k += 1
if b % 2 != 0 and e % 2 == 0:
    for i in range(b, e, 2):
        k += 1
if b % 2 == 0 and e % 2 != 0:
    for i in range(b + 1, e + 1, 2):
        k += 1
if b % 2 != 0 and e % 2 != 0:
    for i in range(b, e + 1, 2):
        k += 1

print(k)

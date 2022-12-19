from itertools import product

k = 0
for x in product('ЗЕРКАЛО', repeat=6):
    s = ''.join(x)
    if s.count('К') == 1 and s.count('А') == 3:
        k += 1
print(k)

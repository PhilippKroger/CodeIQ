from itertools import product

k = 0
for x in product('ABC', 'ABC', 'ABC', 'ABC', 'ABCX'):
    s = ''.join(x)
    k += 1
print(k)

from itertools import product

k = 0
for x in product('ЭЮЯ', 'АБВГ', 'АБВГ', 'АБВГ', 'ЭЮЯ'):
    s = ''.join(x)
    k += 1
print(k)

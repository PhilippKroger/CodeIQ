from itertools import product

k = 0
for x in product('ЖИРА','ЖИРАФ','ЖИРАФ','ЖИРАФ','ЖИАФ'):
    s = ''.join(x)
    if s.count('Ж') == 1:
        k += 1
print(k)

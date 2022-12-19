from itertools import product

k = 0
for x in product('АНИМЕ', repeat=6):
    s = ''.join(x)
    if s.count('Е') == 3:
        k += 1
print(k)
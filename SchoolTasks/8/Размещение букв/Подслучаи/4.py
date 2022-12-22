from itertools import product
k = 0
for x in product('ЖИРАФ', repeat=5):
    s = ''.join(x)
    if s.count('Ж') == 1 and s[0] != 'Ф' and s[-1:] != 'Р':
        k += 1

print(k)
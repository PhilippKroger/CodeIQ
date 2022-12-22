from itertools import permutations

k = 0
for x in permutations('КАЛИЙ'):
    s = ''.join(x)
    if s[0] != 'Й' and 'ИА' not in s:
        k += 1
print(k)
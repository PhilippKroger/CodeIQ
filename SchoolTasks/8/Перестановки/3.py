from itertools import permutations

k = 0
for x in permutations('ПЕСКАРЬ'):
    s = ''.join(x)
    # if s[0]!='Ь' and 'ЬА' not in s and 'ЬЕ' not in s and 'ЬР' not in s:
    if s[0] != 'Ь' and all(sub not in s for sub in ['ЬЕ', 'ЬР', 'ЬА']):
        k += 1
print(k)

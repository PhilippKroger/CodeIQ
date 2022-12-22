from itertools import permutations

k = 0
w = ['ОУ', 'УО', 'КЛ', 'ЛК', 'КН', 'НК', 'ЛН', 'НЛ']
for x in permutations('КОЛУН'):
    s = ''.join(x)
    if all(sub not in s for sub in w):
        k += 1

print(k)

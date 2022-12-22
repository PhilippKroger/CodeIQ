from itertools import permutations

k = 0
for x in set(permutations('АССАСИН')):
    k += 1
print(k)

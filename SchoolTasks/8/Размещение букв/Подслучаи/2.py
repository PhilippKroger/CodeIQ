from itertools import product

#  first way
k1 = 0
for x in product('АНИМЕ', repeat=4):
    k1 += 1
k2 = 0
for x in product('АНИМЕ', repeat=5):
    k2 += 1
k3 = 0
for x in product('АНИМЕ', repeat=6):
    k3 += 1
print(k1 + k2 + k3)
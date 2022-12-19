from itertools import product

k = 0
for x in product('ЛЕТО', repeat=4):
    s = ''.join(x)
    if s[0] in 'ЛТ':
        k += 1
print(k)

# !!!
k = 0
for x in product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО'):
    s = ''.join(x)
    k += 1
print(k)

# Its shit
k = 0
for a in 'ЛЕТО':
    for b in 'ЛЕТО':
        for c in 'ЛЕТО':
            for d in 'ЛЕТО':
                s = a+b+c+d
                if s[0] in 'ЛТ':
                    k += 1
print(k)


# !!!
k1 = 0
for a in 'ЛТ':
    for b in 'ЛЕТО':
        for c in 'ЛЕТО':
            for d in 'ЛЕТО':
                s = a+b+c+d
                k1 += 1
print(k1)

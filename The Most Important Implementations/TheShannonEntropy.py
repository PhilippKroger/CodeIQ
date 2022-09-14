"""
Information entropy is a measure of the uncertainty of the certainty of a system,
in particular, the accuracy of detecting any regular reading character.
"""


from math import log

def entropy_wht_shannon(s):
    d = {}
    h = 0
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for k in d:
        p = d[k] / len(s)
        h += p * log(1 / p, 2)
    return h * len(s)

s = input()
print(entropy_wht_shannon(s))

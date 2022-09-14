"""

Count the number of Duplicates
Write a function that will return the count
of distinct case-insensitive alphabetic
characters and numeric digits that occur
more than once in the input string.
The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""


def duplicate_count(text):
    d = {}
    ntext = []
    for i in range(len(text)):
        ntext.append(text[i].lower())
    for i in range(len(ntext)):
        t = ntext[i]
        if ntext[i] not in d: d[t] = 0
        if ntext[i] in d: d[t] += 1
    dv = d.values()
    dv = list(map(int, dv))
    k_dv = 0
    for i in range(len(dv)):
        if dv[i] > 1:
            k_dv += 1
    if len(dv) == 0: return 0
    if max(dv) == 1: return 0
    if k_dv > 1: return k_dv
    if k_dv == 1: return 1


print(duplicate_count("abcdeaa"))  # 1

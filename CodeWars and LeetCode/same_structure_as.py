def same_structure_as(original, other):

    original = str(original)
    other = str(other)

    new_original = ''
    new_other = ''

    for i in range(len(original)):
        if original[i] in '[],':
            new_original += original[i]
    for i in range(len(other)):
        if other[i] in '[],':
            new_other += other[i]

    new_original_rev = new_original[::-1]
    new_original_rev_d = ''
    for i in range(len(new_original_rev)):
        if new_original_rev[i] == ']':
            new_original_rev_d += '['
        elif new_original_rev[i] == '[':
            new_original_rev_d += ']'
        else:
            new_original_rev_d += new_original_rev[i]
    #  print(new_original_rev_d)
    if new_other == new_original or new_other == new_original_rev_d:
        return True
    else:
        return False


print(same_structure_as([1,'[',']'],['[',']',1])) # [,'[',']'], ['[',']',]


"""
Write an algorithm that takes
an array and moves all of the
zeros to the end, preserving
he order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3])
# returns [1, 1, 2, 1, 3, 0,
"""


def move_zeros(lst):
    new_lst = []
    k = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            new_lst.append(lst[i])
        else:
            k += 1
    for i in range(k):
        new_lst.append(0)
    return new_lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))  # returns [1, 1, 2, 1, 3, 0, 0]

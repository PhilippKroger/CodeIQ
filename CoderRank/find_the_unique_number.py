"""

There is an array with some numbers.
All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

"""


def find_uniq(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d:
            di = arr[i]
            d[di] = 1
        else:
            di = arr[i]
            d[di] += 1
    for k, v in d.items():
        if v == 1:
            return k


print(find_uniq([1, 1, 2, 1, 1, 1]))  # 2

"""
Write a function that accepts an array of 10 integers
(between 0 and 9), that returns a string of those numbers
in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""


def create_phone_number(n):
    a = ''
    b = ''
    c = ''

    for i in range(len(n)):
        if i < 3:
            a += str(n[i])
        if 6 > i > 2:
            b += str(n[i])
        if i > 5:
            c += str(n[i])

    return "(" + str(a) + ") " + str(b) + "-" + str(c)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

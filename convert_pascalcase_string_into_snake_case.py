"""
https://www.codewars.com/kata/529b418d533b76924600085d/train/python
"""

def to_underscore(string):
    s = ''
    for i in range(len(string)):
        if i == 0 and string[i].isupper():
            s += string[i].lower()
            continue
        elif string[i].isupper():
            s += '_' + string[i].lower()
        elif string[i].islower() and string[i] not in "0":
            s += string[i]

print(to_underscore("TestController"))
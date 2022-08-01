"""

Complete the solution so that
the function will break up camel
casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""

def solution(s):
    new_s = ''
    for i in range(len(s)):
        if s[i].isupper():
            new_s += ' '
            new_s += s[i]
        else:
            new_s += s[i]
    return new_s

print(solution("camelCasing"))  # camel Casing
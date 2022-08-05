"""
Complete the function/method so that it takes
a PascalCase string and returns the string in
snake_case notation. Lowercase characters can be numbers.
If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
"""

def to_underscore(string):
    string = str(string)
    s = ''
    for i in range(len(string)):
        if i == 0 and string[i].isupper():
            s += string[i].lower()
            continue
        elif string[i].isupper():
            s += '_' + string[i].lower()
        elif string[i].isdigit():
            s += string[i]
        elif string[i].islower() and string[i] not in "0":
            s += string[i]
    return s

print(to_underscore("TestController"))

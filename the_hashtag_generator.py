"""

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""


def generate_hashtag(s):
    s = s.split()
    s1 = []
    for i in range(len(s)):
        s1.append(s[i][0].upper()+s[i][1:].lower())
    st = "".join(s1)
    if len(st) == 0:
        return False
    elif len(st) >= 140:
        return False
    else:
        return "#" + st

print(generate_hashtag("CodeWars is nice"))
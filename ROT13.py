"""
ROT13 is a simple letter substitution cipher
that replaces a letter with the letter 13
letters after it in the alphabet. ROT13
is an example of the Caesar cipher.

Create a function that takes a string
and returns the string ciphered with Rot13.
If there are numbers or special characters
included in the string, they should be
returned as they are. Only letters from
the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


alphabet = "abcdefghijklmABCDEFGHIJKLMnopqrstuvwxyzNOPQRSTUVWXYZ"
def rot13(message):
    """We have Caesar's cipher with c_key -> 13"""
    rot13_message = ''
    for i in message:
        if i == '':
            rot13_message += ''
        if i in alphabet:
            x = alphabet.find(i)
            y = (x + 26) % (len(alphabet))
            rot13_message += alphabet[y]
        else:
            rot13_message += i
    return rot13_message


print(rot13("10+2 vf gjryir."))  # Output: 10+2 is twelve.

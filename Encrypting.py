alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def caesar_cipher(message, key):
    """Encrypting a message with a Caesar cipher"""
    b = ''
    for i in message:
        if i == ' ':
            b += ' '
        else:
            x = alphabet.find(i)
            y = (x + key) % (len(alphabet))
            b += alphabet[y]
    return b


print(caesar_cipher('ПРИВЕТ', 3))  # Your message and letter shift


def caesar_cipher_decoder(message, key):
    """Decoding a message encrypted with a Caesar cipher"""
    a = ''
    for x in message:
        if x == ' ':
            a += ' '
        else:
            x = alphabet.find(x)
            y = x - key
            a += alphabet[y]
    return a


print(caesar_cipher_decoder('ПРИВЕТ', 3))  # Your message and letter shift


def vigenere_cipher(message, key):
    """Encrypting a message with a Vigenere cipher"""
    k = []
    for i in range(len(key)):
        k.append(alphabet.find(key[i]))
    b = ''
    for i in range(len(message)):
        x = alphabet.find(message[i])
        y = (x + k[i % len(k)]) % (len(alphabet))
        b += alphabet[y]
    return b


print(vigenere_cipher('ПРИШЕЛ ПРИШЕЛ', 'ЗАБЕГ'))

# a program for decoding a message written in the Vigenère cipher,
# identical, only + must be changed to -

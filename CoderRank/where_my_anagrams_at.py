"""
What is an anagram? Well,
two words are anagrams of each other
if they both contain the same letters. For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all
the anagrams of a word from a list.
You will be given two inputs a word
and an array with words. You should
return an array of all the anagrams
or an empty array if there are none.
For example: anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
"""

def anagrams(word, words):
    all_words = []
    for i in range(len(words)):
        if sorted(list(word)) == sorted(list(words[i])):
            all_words.append(words[i])
    return all_words

print(anagrams("abba", ['bbaa', 'abcd']))
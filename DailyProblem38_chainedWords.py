"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

Given a list of words, determine if there is a way to 'chain' all the words in a circle.

Example:
Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
Output: True
Explanation:
The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

Here's a start:

from collections import defaultdict

def chainedWords(words):
  # Fill this in.

print chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna'])
# True

"""
from collections import defaultdict

def chainedWords(words):
    dic = {}
    for word in words:
        s = word[0]
        e = word[-1]
        dic[s] = e

    for word in words:
        s = word[0]
        e = word[-1]
        # new_s = dic[e]
        del dic[e]
    return len(dic) == 0



print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
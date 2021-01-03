"""
Hi, here's your problem today. This problem was recently asked by Google:

Given two strings, find if there is a one-to-one mapping of characters between the two strings.

Example
Input: abc, def
Output: True # a -> d, b -> e, c -> f

Input: aab, def
Ouput: False # a can't map to d and e 
Here's some starter code:

def has_character_map(str1, str2):
  # Fill this in.

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
"""
def has_character_map(s, t):
    s2t, t2s = {}, {}
    for i in range(len(s)):
        if s[i] in s2t and s2t[s[i]] != t[i]:
            return False
        if t[i] in t2s and t2s[t[i]] != s[i]:
            return False
        s2t[s[i]] = t[i]
        t2s[t[i]] = s[i]
    return True

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
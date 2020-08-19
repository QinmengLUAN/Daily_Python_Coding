"""
242. Valid Anagram
Easy: Hash Table, Array

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def 3(self, s: str, t: str) -> bool:
        c_s = Counter(s)
        c_t = Counter(t)
        
        for k in c_s:
            if c_s[k] != c_t[k]:
                return False
        return len(c_s) == len(c_t)
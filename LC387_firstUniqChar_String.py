"""
387. First Unique Character in a String
Easy: String, Hash Table

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        res = len(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                res = min(res, i)
        return res if res != len(s) else -1
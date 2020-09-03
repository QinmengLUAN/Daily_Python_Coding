"""
3. Longest Substring Without Repeating Characters
Medium: Hash Table, Two Pointers, String, Sliding Window
Microsoft

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        seen = {}
        seen[s[0]] = 0
        
        l, r = 0, 1
        res = 1
        while r < len(s):
            # print(l, r)
            if s[r] not in seen:
                seen[s[r]] = r
                res = max(r-l+1, res)
                r += 1
            else: 
                for k in range(l, seen[s[r]]):
                    if s[k] in seen:
                        del seen[s[k]]
                l = seen[s[r]] + 1
                seen[s[r]] = r
                r += 1
            # print(seen)
        return res
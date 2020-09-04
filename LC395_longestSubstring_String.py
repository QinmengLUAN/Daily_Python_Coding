"""
395. Longest Substring with At Least K Repeating Characters
Medium: String Recursion

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
"""
Solution:
If every character appears at least k times, the whole string is ok. 
Otherwise split by a least frequent character (because it will always be too infrequent 
and thus can't be part of any ok substring) and make the most out of the splits.

As usual for Python here, the runtime varies a lot, 
this got accepted in times from 32 ms to 74 ms.
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))
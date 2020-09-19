"""
409. Longest Palindrome
Easy: String

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2

"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        C = Counter(s)
        odd, res = 0, 0
        for c in C:
            odd = max(C[c]%2, odd)
            res += (C[c]//2) * 2
        res += odd
        return res
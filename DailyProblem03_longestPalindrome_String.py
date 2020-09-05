"""
Hi, here's your problem today. This problem was recently asked by Twitter:
Leetcode 409
A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
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
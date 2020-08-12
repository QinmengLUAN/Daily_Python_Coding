"""
231. Power of Two
Easy: Math

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""
class Solution:
    # Math
    def isPowerOfTwo1(self, n: int) -> bool:
        return n > 0 and (2**30 % n == 0)
    # Iteration
    def isPowerOfTwo2(self, n: int) -> bool:    
        if (n <= 0):
            return False
        while n%2 == 0:
               n/=2
        return n == 1
    # Recursion
    def isPowerOfTwo(self, n: int) -> bool:     
        return n > 0 and (n == 1 or (n%2 == 0 and self.isPowerOfTwo(n/2)))
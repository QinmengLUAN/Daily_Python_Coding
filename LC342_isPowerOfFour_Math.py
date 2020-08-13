"""
342. Power of Four
Easy: Loop

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfFour1(self, num: int) -> bool:
        if (num <= 0):
            return False
        while num % 4 == 0:
               num //= 4
        return num == 1

    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num
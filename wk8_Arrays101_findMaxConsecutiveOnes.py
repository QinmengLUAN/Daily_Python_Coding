"""
485. Max Consecutive Ones
Easy: Array101

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        max_ones = 0
        for item in nums:
            if item == 1:
                i += 1
                max_ones = max(i,max_ones)
            else:          
                i = 0
        return max_ones
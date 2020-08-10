"""
268. Missing Number
Easy: Array

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)
        
        
    def missingNumber1(self, nums: List[int]) -> int:        
        l = len(nums)
        res = {i for i in range(l)}
        for n in nums:
            if n in res:
                res.remove(n)
        # print(res)
        if len(res) == 0:
            return l
        else:
            return res.pop()
"""
15. 3Sum
Medium: Array, Binary Search

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # print(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if 0 < k and nums[k] == nums[k-1]:
                continue
            target = 0 - nums[k]
            i = k + 1
            j = len(nums) - 1
            while k < i < j:
                nfit = nums[i] + nums[j]
                if nfit < target:
                    i += 1
                elif nfit > target:
                    j -= 1
                elif nfit == target:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i<j:
                        i += 1
                    while nums[j] == nums[j+1] and i<j:
                        j -= 1
        return res
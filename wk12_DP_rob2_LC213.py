"""
213. House Robber II
Medium: DP 
Solution: consider 2 possible cases: rob the first house or not

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(self.simple_rob(nums, 1, n), self.simple_rob(nums, 0, n-1))
        
    def simple_rob(self, nums, i, j):
        rob, not_rob = 0, 0
        for idx in range(i, j):
            num = nums[idx]
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)
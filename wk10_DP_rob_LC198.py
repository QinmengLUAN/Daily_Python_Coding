"""
198. House Robber
Easy: DP, space complexity O(N) or O(1), time compaxity O(N)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
# Space constant O(N)
# Simplify the nums list into three items, always consider either robbing the thrid door + first door, or the second door instead
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            res = [0] * len(nums)
            res[0], res[1] = nums[0], max(nums[0], nums[1])
            for i in range(2,len(nums)):
                res[i] = max(res[i-2] + nums[i], res[i-1])
        return res[-1]
"""
# Constant space
class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            first_house, second_house = nums[0], max(nums[0], nums[1])
            for i in range(2,len(nums)):
                thrid_house = max(first_house + nums[i], second_house)
                first_house = second_house
                second_house = thrid_house
        return thrid_house

nums = [4,1,1,4]
s = Solution()
print(s.rob(nums))

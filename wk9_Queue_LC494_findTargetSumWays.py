"""
494. Target Sum
Medium: Queue, recursion, DFS
Time complexity: O(N^2)
Space complexity: O(N)

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""
class Solution:
    def findTargetSumWays(self, nums, S):
        return self.helper(nums, S, 0, 0)

    def helper(self, nums, S, i, curr_sum):
        if i == len(nums):
            if curr_sum == S:
                return 1
            else:
                return 0    
        return self.helper(nums, S, i + 1, curr_sum + nums[i]) + self.helper(nums, S, i + 1, curr_sum - nums[i])

nums = [1, 1, 1, 1, 1]
S = 3
s = Solution()
print(s.findTargetSumWays(nums, S))
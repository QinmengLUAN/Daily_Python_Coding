"""
18. 4Sum
Medium
Qorks for N-sum (N>=2)

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution:
    # Fast solution:
    # The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum. Some optimization was be made knowing the list is sorted.
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.findNsum(0, len(nums)-1, nums, target, 4, [], results)
        return results
    def findNsum(self, l, r, nums, target, N, curr, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        elif N == 2:
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(curr + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1     
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    self.findNsum(i+1, r, nums, target-nums[i], N-1, curr+[nums[i]], results)
        
        
    # Slow DFS method
    # Time O(n^3), space O(n*n)
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, curr_list = [], []
        self.dfs(nums, target, 0, res, curr_list)
        return res
        
    def dfs(self, nums, target, idx, res, curr_list):
        # early termination
        if len(nums) < 4 or len(curr_list) > 4 or target < nums[0] * (4-len(curr_list)) or target > nums[-1] * (4-len(curr_list)):
            return
        if len(curr_list) == 4:
            if target == 0:
                # print(curr_list)
                res.append(curr_list.copy())
            return
        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i-1]:
                continue
            curr_list.append(nums[i])
            self.dfs(nums, target - nums[i], i + 1, res, curr_list)
            curr_list.pop()
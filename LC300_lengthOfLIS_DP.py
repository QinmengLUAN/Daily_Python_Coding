"""
300. Longest Increasing Subsequence
Medium: DP

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #  Check cornor cases      
        if len(nums) <= 1:
            return len(nums)
        
        #  Initiate the DP table   
        dp = [1] * len(nums)
        
        #  Table filling
        #  transition function: dp[i] = max(dp[j] + 1), j < i && nums[j] < nums[i] 
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        #  Any position could be the result
        return max(dp)
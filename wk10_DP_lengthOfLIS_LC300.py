"""
300. Longest Increasing Subsequence
Medium: DP
----------------------------------------------------------
tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6
We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:
(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
----------------------------------------------------------
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
    # O(NlogN) time complexity due to binary search, O(N) space complexity, 
    def lengthOfLIS_2(self, nums):
        tails = [0] * len(nums)
        size = 0

        for k in range(len(nums)):
            # Binary search below, i,j are the pivot
            i, j = 0, size 
            while i != j:
                m = (i + j) // 2
                if tails[m] < nums[k]:
                    i = m + 1
                else:
                    j = m
            tails[i] = nums[k]
            size = max(i + 1, size)
        # print(tails)
        return 

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0

        for k in range(len(nums)):
            # find 1st element that is larger than current num
            # if none, append num to the end
            for i in range(size+1):
                if i == size or nums[k] < tails[i]:
                    break
            tails[i] = nums[k]
            size = max(i + 1, size)
        
        print(tails)
        return size

s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))




"""
581. Shortest Unsorted Continuous Subarray
Easy: Array, time complexity O(n)

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        for s in range(n):
            if s == n-1:
                return 0
            elif nums[s] > nums[s+1]:
                break

        for e in range(n-1, 0, -1):
            if nums[e] < nums[e-1]:
                break
        
        max_val = max(nums[s:e+1])
        min_val = min(nums[s:e+1])

        for i in range(s):
            if nums[i] > min_val:
                s = i
                break
        for i in range(n-1, e, -1):
            if nums[i] < max_val:
                e = i
                break

        return e-s+1

    
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l, r = 0, len(nums) - 1
        
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1
            
        if l > r:
            return 0
        
        temp_min = min(nums[l:r+1])
        temp_max = max(nums[l:r+1])
        
        while l > 0 and temp_min < nums[l - 1]:
            l -= 1
        
        # Be careful with conditions for while loop
        while r < len(nums) - 1 and temp_max > nums[r + 1]:
            r += 1
            
        return r - l + 1

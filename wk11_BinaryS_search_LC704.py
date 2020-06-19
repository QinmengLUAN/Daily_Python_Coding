"""
704. Binary Search
Easy: Be careful with the corner case

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Return -1 for impossible cases first
        if len(nums) < 1 or nums[0] > target or nums[-1] < target:
            return -1
        # Exclude boundary cases first
        l, r = 0, len(nums) - 1       
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        while r - l > 1:
            # Safer way to get mid
            mid = l + (r - l) // 2         
            if nums[mid] < target:
                l = mid               
            elif nums[mid] > target:
                r = mid           
            elif nums[mid] == target:
                return mid
        return -1

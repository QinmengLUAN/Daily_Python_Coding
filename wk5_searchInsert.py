"""
Leetcode 35. Search Insert Position
Easy: Binary Search_Be careful with the corner cases

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    if target <= nums[0]:
        return 0
    elif target == nums[-1]:
        return len(nums) - 1
    elif target > nums[-1]:
        return len(nums)
    
    while left >= 0 and right < len(nums):
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
        if (right - left) == 1:
            return right

inp = [1,3,5,6]
tar = 7
print(searchInsert(inp, tar))
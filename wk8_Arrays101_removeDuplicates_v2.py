"""
26. Remove Duplicates from Sorted Array
Easy: Array: O(1) space, O(n) time

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""
class Solution:
    def removeDuplicates(self, nums):
        slow = fast = 0
        while fast < len(nums) - 1:
            fast += 1
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow += 1
        return slow + 1

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))

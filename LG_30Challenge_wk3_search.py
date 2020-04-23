"""
33. Search in Rotated Sorted Array
Medium: Binary Search, Array, O(log n) time complexity

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
"""
4 Possible cases available:
target < i, target < j: target in [i, j] => nums[pivot] > nums[i]: target in [pivot, j]; nums[pivot] < nums[i]:
target < i, target > j: target not in [i, j] =>
target > i, target < j: target in [i, j] =>
target > i, target > j: target in [i, j] =>
"""
class Solution:
    def search(self, nums, target):
        i, j = 0, len(nums) - 1   
        while i <= j:
            pivot = (i + j) // 2
            print(i, j, pivot)
            if i == j and target != nums[i]:
                return -1
            if target == nums[i]:
                return i
            if target == nums[j]:
                return j
            if pivot == i:
                return -1

            if target < nums[i] and target < nums[j]:
                if target == nums[pivot]:
                    return pivot
                elif target < nums[pivot]:
                    if nums[pivot] < nums[j]:
                        j = pivot
                    else:
                        i = pivot
                elif target > nums[pivot]:
                    i = pivot
            elif target < nums[i] and target > nums[j]:
                return -1     
            elif target > nums[i] and target < nums[j]:
                if target == nums[pivot]:
                    return pivot
                if target < nums[pivot]:
                    j = pivot
                if target > nums[pivot]:
                    i = pivot            
            elif target > nums[i] and target > nums[j]:
                if target == nums[pivot]:
                    return pivot
                if target < nums[pivot]:
                    if nums[pivot] > nums[j]:
                        j = pivot 
                    else:
                        i = pivot
                if target > nums[pivot]:
                    if nums[pivot] > nums[i]:
                        i = pivot
                    else:
                        j = pivot
        return -1                  

nums = [4,5,6,7,0,1,2]
target = 0
s = Solution()
print(s.search(nums, target))






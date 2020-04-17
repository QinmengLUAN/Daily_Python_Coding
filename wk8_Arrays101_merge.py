"""
88. Merge Sorted Array
Easy: Array, be careful with line 26: idx < (m + i)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = 0
        for i in range(n):
            while idx < (m + i) and nums2[i] >= nums1[idx]:
                idx += 1
            nums1.insert(idx, nums2[i])
            nums1.pop()
            
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)
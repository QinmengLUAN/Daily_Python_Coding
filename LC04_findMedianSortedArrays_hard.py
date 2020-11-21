"""
4. Median of Two Sorted Arrays
Hard: Two pointer

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0
        left, right = -1, -1 
        for i in range((m + n) // 2 + 1):
            left = right
            # p2 右移
            if p1 >= len(nums1) or p2 < len(nums2) and nums1[p1] > nums2[p2]:
                right = nums2[p2]
                p2 += 1
            # p1 右移
            else:
                right = nums1[p1]
                p1 += 1
        # 长度和是奇数
        if (m + n) % 2 == 1:
            return right
        # 长度和是偶数
        return (left + right) / 2
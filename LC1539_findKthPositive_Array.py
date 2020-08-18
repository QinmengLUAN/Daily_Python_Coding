"""
1539. Kth Missing Positive Number
Easy: Array

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            # print(l, r)
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m  
        return l + k
        
    def findKthPositive1(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        res_list = list(range(1, len(arr_set) + k + 1))
        # print(res_list)
        res = []
        for item in res_list:
            if item not in arr_set:
                res.append(item)
        # print(res)
        return res[k-1]
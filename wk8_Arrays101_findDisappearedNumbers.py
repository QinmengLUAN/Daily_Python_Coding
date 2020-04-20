"""
448. Find All Numbers Disappeared in an Array
Easy: Array, be more careful to the question

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number

        for i in range(len(nums)):
            temp = abs(nums[i]) - 1 #abs() is important
            if nums[temp] > 0:
                nums[temp] *= -1
        #     print(temp, nums[temp]) 
        # print(nums)   
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res

nums = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDisappearedNumbers(nums))
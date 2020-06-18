"""
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
# Solution 1: two pass + dictionary
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        comp_n = len(nums) // 2
        for key in nums_counter:
            if nums_counter[key] > comp_n:
                return key

# Solution 2: 1 pass + dictionary
    def majorityElement(self, nums):
        nums_dic = {}
        for item in nums:
            if item not in nums_dic:
                nums_dic[item] = 1
            else:
                nums_dic[item] += 1
                
            if nums_dic[item] > (len(nums) // 2):
                return item 
# Sotring O(n log n)
# Since you know that the majority element is the element that appears MORE THAN n/2 times, meaning that if you sort the input, then the median number is guaranteed to be the majority element.
# Ex: [1, 4, 3, 1, 1, 5, 1, 1] here (N=8)/2 is 4 meaning that there must be 5 of the majority element. Sorted this is [1, 1, 1, 1, 1, 3, 4, 5]. Where 1 is the majority element.
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
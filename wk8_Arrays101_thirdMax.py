"""
414. Third Maximum Number
Easy: Array

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
class Solution:
    def thirdMax(self, nums):

        if len(set(nums)) < 3:
            return max(nums)
         
        max_num = nums[0]
        second_max = float('-inf')
        third_max = float('-inf')

        for i in range(1,len(nums)):

            if nums[i] > max_num:
                third_max = second_max
                second_max = max_num
                max_num = nums[i]
                
            if max_num > nums[i] > second_max:
                third_max = second_max
                second_max = nums[i]

            if second_max > nums[i] > third_max:
                third_max = nums[i]

            i += 1
        return third_max

inp = [1,2,-2147483648]
s = Solution()
print(s.thirdMax(inp))
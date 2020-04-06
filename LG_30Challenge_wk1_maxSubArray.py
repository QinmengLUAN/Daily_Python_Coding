"""
30 days Leetcode Challenge
wk1: maxSubArray: seems easy, but hard! Remember this.
    Key Points:
        Let's consider a simpler example: [a, b, c]. It has many sub arraries: [a],
        [a, b], [a, b, c], [b, c], etc. Let's assume a < 0, then it's obvious the
        max subarry will not contain a. Because not matter it's [a, b] or [a, b, c],
        removing a will only make it larger. Similarly, if a + b < 0, then [c] itself
        is definitely larger than [a, b, c].
        So, the key point here is, we scan from left to right and memorizing the sum
        so far, once it's < 0, we just completely ignore all previous elements in the
        array, like they never exist. Since no matter what the following elements are,
        they will be larger without the previous elements.
        Of course, the sum may be > 0 first, then we see a large negative number and
        the sum becomes negative. In order not to miss the positive result we ever had,
        we use a global variable to track the max sum ever appearred.
Given an integer array nums, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        curr_so_far = 0
        for item in nums:
            curr_so_far += item
            max_so_far = max(max_so_far, curr_so_far)
            curr_so_far = max(0, curr_so_far)
        return max_so_far
nums = [-2,1,-3,4,-1,2,1,-5, -2]
s = Solution()
print(s.maxSubArray(nums))

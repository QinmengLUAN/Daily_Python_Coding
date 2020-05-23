'''
487 Max Consecutive Ones II
Medium: Array, line 27&28 is important
Problem:
Given a binary array, 
find the maximum number of consecutive 1s in this array 
if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
After flipping, the maximum number of consecutive 1s is 4.
Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
'''
class Solution:
    def findMaxConsecutiveOnesII(self, nums):
        pre_num = curr_num = max_num = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                pre_num += 1
            else:
                curr_num = pre_num + 1
                pre_num = 0
            max_num = max(curr_num + pre_num, max_num)
            # print(i, pre_num, curr_num, max_num)
        return max_num

nums = [1,0,1,1,0]
s = Solution()
print(s.findMaxConsecutiveOnesII(nums))
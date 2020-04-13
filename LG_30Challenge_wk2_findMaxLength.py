"""
525. Contiguous Array
Medium: Hash table, dictionary, thinking is important

Given a binary array, 
find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
class Solution:
    def findMaxLength(self, nums):
        label = 0
        dict_label = {}
        dict_label[0] = 0
        max_length = 0

        for i in range(len(nums)):
            label += (nums[i]*2 - 1)
            ## The above line means below: 
            # if nums[i] == 1:
            #     label += 1
            # else:
            #     label -= 1
            if label in dict_label: # check wether the value has appeared
                idx = dict_label[label]
                max_length = max(i - idx + 1, max_length)
            else:
                dict_label[label] = (i + 1)
        return max_length

nums = [0, 1,0,1, 1]
s = Solution()
print(s.findMaxLength(nums))
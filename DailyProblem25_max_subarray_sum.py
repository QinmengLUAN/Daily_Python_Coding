"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.

Here's a starting point:

def max_subarray_sum(arr):
  # Fill this in.

print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137

"""
def max_subarray_sum(nums):
    if len(nums) == 0:
        return 0
    max_so_far = nums[0]
    curr_so_far = 0
    for n in nums:
        curr_so_far += n
        max_so_far = max(max_so_far, curr_so_far)
        curr_so_far = max(0, curr_so_far)
    return max_so_far

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
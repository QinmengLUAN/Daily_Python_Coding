"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.

Here's your starting point:

def first_missing_positive(nums):
  # Fill this in.

print first_missing_positive([3, 4, -1, 1])
# 2
"""
def first_missing_positive(nums):
    max_num = max(nums)
    res = [i for i in range(max_num + 1)]
    for num in nums:
        if num > 0:
            res[num] = 0
    for r in res:
        if r != 0:
            return r
    return None

print(first_missing_positive([3, 4, -1, 1]))
# 2
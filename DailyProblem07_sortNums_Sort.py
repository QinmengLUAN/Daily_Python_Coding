"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
  # Fill this in.

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
"""
def sortNums(nums):
# Fill this in.
    i, j, k = 0, 0, 0
    for n in nums:
        if n == 1:
            i += 1
        if n == 2:
            j += 1
        else:
            k += 1
    for m in range(len(nums)):
        if m < i:
            nums[m] = 1
        elif m < i+j:
            nums[m] = 2
        else:
            nums[m] = 3
    return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
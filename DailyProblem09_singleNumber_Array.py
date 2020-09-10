"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.
"""
def singleNumber1(nums):
  # Fill this in.
    res = 0
    for num in nums:
        res ^= num
    return res

from collections import Counter
def singleNumber(nums):
    C = Counter(nums)
    for c in C:
        if C[c] == 1:
            return c


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
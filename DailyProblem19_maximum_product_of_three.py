"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by 
multiplying -4 * -4 * 8 = 128.

Here's a starting point:

def maximum_product_of_three(lst):
  # Fill this in.

print maximum_product_of_three([-4, -4, 2, 8])
# 128
"""
def maximum_product_of_three(nums):
  # Fill this in.
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
"""
Hi, here's your problem today. This problem was recently asked by Apple:

A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the index and value is the same. 
Find a fixed point (there can be many, just return 1) in a sorted list of distinct elements, or return None if it doesn't exist.

Here is a starting point:

def find_fixed_point(nums):
  # Fill this in.

print find_fixed_point([-5, 1, 3, 4])
# 1
"""
# Method 1: O(N)
def find_fixed_point1(nums):
    for i in range(len(nums)):
        if nums[i] == i:
            return i
    return None

print(find_fixed_point1([-5, 1, 3, 4]))
# 1
print(find_fixed_point1([-10, -1, 0, 3, 10, 11, 30, 50, 100]))
# 3


# Method 2: Binary search O(Log N)
def find_fixed_point(nums):
    l, r = 0, len(nums) - 1
    return bs(nums, l, r)

def bs(nums, l, r):
    if r == nums[r]:
        return r
    elif l == nums[l]:
        return l

    while r > l + 1:
        mid = (r + l) // 2
        if mid == nums[mid]:
            return mid
        elif mid > nums[mid]:
            l = mid
        else:
            r = mid
    return None

print(find_fixed_point([-5, 1, 3, 4]))
# 1
print(find_fixed_point([-10, -1, 0, 3, 10, 11, 30, 50, 100]))
# 3
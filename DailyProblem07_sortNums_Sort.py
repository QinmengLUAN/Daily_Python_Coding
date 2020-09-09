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
    i, k, j = 0, 0, len(nums)-1
    while k <= j:
        if nums[k] == 1 and k != i:
            tmp = nums[i]
            nums[i] = nums[k]
            nums[k] = tmp
            i += 1
        elif nums[k] == 3:
            tmp = nums[j]
            nums[j] = nums[k]
            nums[k] = tmp
            j -= 1
        else:
            k += 1
        # print(nums, i, j, k)
    return nums
def sortNums1(nums):
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

print(sortNums([3, 1, 2, 1, 3, 2, 1]))
print(sortNums([3, 2, 2, 1, 3, 3, 1]))
print(sortNums([2, 3, 1]))

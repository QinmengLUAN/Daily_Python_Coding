"""
Hi, here's your problem today. This problem was recently asked by Microsoft:
Leetcode 665
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

Here is the function signature:

def check(lst):
  # Fill this in.

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False

Can you find a solution in O(n) time?
从头开始模拟，碰到第一次nums[i]<nums[i-1]时，
我们需要修改nums[i]或者nums[i-1]来保证数组的不下降。 
有两种情况： 1、nums[i]<nums[i-2]，比如3,4,2这样的情况，当前nums[i]=2。此时我们只能将nums[i]修改为4，才能在满足题意的条件下保证数组不下降，修改后为3,4,4。 
2、nums[i]>=nums[i-2]，比如3,5,4，当前nums[i]=4。此时我们可以将nums[i-1]修改为4，修改后为3,4,4。
"""
def check(nums):
  # Fill this in.
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            count += 1
            if i >= 2 and nums[i] < nums[i - 2]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]
    return count <= 1
 
print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False
print(check([1,1,0,0,3,3]))
# False
print(check([1,9,1, 1]))
# True
print(check([1]))
# True
print(check([7, 8, 9, 1, 1, 11]))
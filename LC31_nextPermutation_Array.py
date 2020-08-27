"""
31. Next Permutation
Medium: Array

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                for j in range(len(nums) - 1, idx, -1):
                    if nums[j] > nums[idx]:
                        tmp = nums[j]
                        nums[j] = nums[idx]
                        nums[idx] = tmp
                        break
                # print(nums)
                nums[idx + 1:] = reversed(nums[idx + 1:])
                return nums
        return nums.reverse()
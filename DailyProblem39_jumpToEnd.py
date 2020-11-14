"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers, find the minimum number of jumps to reach the end of the list.

Example:
Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2
Explanation:

The minimum number of jumps to get to the end of the list is 2:
3 -> 5 -> 4

Here's a starting point:

def jumpToEnd(nums):
  # Fill this in.

print jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])
# 2
"""
# Method 1: Dynamic programming
# dp[i] = min(dp[i], dp[j] + 1)
# Time complexity: O(N^2)
# Space complexity: O(N)

def jumpToEnd(nums):
    dp = [i+1 for i in range(len(nums))]
    dp[0] = 0
    # print(dp)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] + j >= i:
                dp[i] = min(dp[i], dp[j] + 1)
                break
    return dp[-1]

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
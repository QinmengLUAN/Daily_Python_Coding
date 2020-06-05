"""
55. Jump Game
Medium: DP
-------------------------------------------------------------
Solution:
f[j] is whether the fog can jump to the stone
Transition function: f[j] = OR_0<=i<j (f[i] AND i+a[j] >=j)
Initial state: f[0] = 0
Calculate f[1], f[2], ..., f[n-1]
Answer is: f[n-1]
Time complexity O(N^2) Space complexity O(N)
--------------------------------------------------------------
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
class Solution:
    def canJump(self, nums):
        f = [False] * len(nums)
        f[0] = True
        for j in range(1,len(nums)):
            # previous stone i
            # last jump from i to j
            # [::-1] is to reduce the calculation time
            for i in range(j)[::-1]:
                if i < j:
                    if f[i] == True and i + nums[i] >= j:
                        f[j] = True
        return f[-1]

s = Solution()
nums = [2,3,1,1,4]
print(s.canJump(nums))

























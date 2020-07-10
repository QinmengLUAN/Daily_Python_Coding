"""
416. Partition Equal Subset Sum
Medium: DP, Knapsack problem

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanat
"""
"""
Solution:
1.判断是否可以将一个数组划分为两个元素和相同的子数组，假设总元素和为sum且sum是偶数，那么划分的两个子数组元素和为sum/2；若sum为奇数则无解。因此，我们可以将这题转化为求“从给定数组中选取元素放入容量为sum/2的背包，询问是否能装满”的问题。
2.令dp[i]表示是否有这样一种可行方案使得元素和为i，则状态转移方程： dp[i] = dp[i] or dp[i - x]
3.即对于元素x，对于已存在的每一个元素和∈[x,sum/2]，都要重新判断可行性：已经可行或者现在加上x可行都算可行，否则算不可行。
Complexity:
假设有n个元素，元素总和为m；
空间复杂度为O(m);
时间复杂度为O(n*m)。
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half = sum(nums) // 2
        
        dp = [False for i in range(half + 2)]
        dp[0] = True
        for x in nums:
            for i in range(half, x - 1, -1):
                dp[i] = dp[i] or dp[i-x]
        # print(dp)
        return dp[half]
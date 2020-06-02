'''
70. Climbing Stairs
Easy: DP, fibonacci
Time complexity: O(N)
Space complexity: O(N)

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
# Method 1: Memorization, top down
class Solution:   
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})

    def helper(self, n, cache):
        if n <= 2:
            return max(0, n)
        elif n in cache:
            return cache[n]
        else:   
            res = self.helper(n - 1, cache) + self.helper(n - 2, cache)
            cache[n] = res
            return res

# Method 2: Table filling, bottom up
class Solution:   
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return max(0, n)
        stored_res = {1:1, 2:2}
        i = 3
        while i <= n:
            stored_res[i] = stored_res[i - 1] + stored_res[i - 2]
            i += 1
        return stored_res[n]
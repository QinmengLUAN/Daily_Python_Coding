"""
322. Coin Change
Medium: DP, time complexity O(m*n), m is amount, n is the choice of coins

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""
# Transition function f(n) = min(f(n - 1), f(n - 2), f(n - 5)) + 1
class Solution:
    def coinChange(self, coins, amount):
        res = {}
        res[0] = 0
        for i in range(1, amount + 1):
            res[i] = amount + 1
        # print(res)
        for i in range(len(res)):
            for j in range(len(coins)):
                if i >= coins[j]:
                    res[i] = min(res[i], res[i - coins[j]] + 1)
        # print(res)
        if res[amount] != amount + 1:
            return res[amount]
        else:
            return -1

s = Solution()
coins = [2]
amount = 3
print(s.coinChange(coins, amount))
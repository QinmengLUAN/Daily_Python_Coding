"""
464. Can I Win
Medium: DP

In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise return false. Assume both players play optimally.

 

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0: return True
        choices = set([i for i in range(1, maxChoosableInteger + 1)])
        return self.dfs_helper(choices, desiredTotal, {})
            
    def dfs_helper(self, choices, desiredTotal, cache):
        if sum(choices) < desiredTotal or desiredTotal <= 0:
            return False
        if len(choices) == 0:
            return False
        if max(choices) >= desiredTotal:
            return True
        
        cachekey = str(sorted(choices))
        if cachekey not in cache:
            cache[cachekey] = {}
        elif desiredTotal in cache[cachekey]:
            return cache[cachekey][desiredTotal]
        
        for c in list(choices):
            canWin = True
            choices.remove(c)
            for t in list(choices):
                choices.remove(t)
                canWin &= self.dfs_helper(choices, desiredTotal - c - t, cache)
                choices.add(t)
                if not canWin:
                    break
            choices.add(c)
            if canWin:
                cache[cachekey][desiredTotal] = True
                return True
        cache[cachekey][desiredTotal] = False
        return False
class Solution:
    """
    @param maxChoosableInteger: a Integer
    @param desiredTotal: a Integer
    @return: if the first player to move can force a win
    """

    def canIWin(self, maxChoosableInteger, desiredTotal):
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, desiredTotal):

        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                self.memo[hash] = True
                return True
        self.memo[hash] = False
        return False
"""
1049. Last Stone Weight II
Medium

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
"""

"""
Explain:
Explaining why this problem is equals to finding the difference between the sum of two groups

Suppose you have rock a, b, c and d.
If you subtract them in the following order: b-c, then d-(b-c). Then it is the same as doing d-b+c.
Then doing (d-b+c)-a is the same as -a+d-b+c, which is d+c-a-b, which is (d+c)-(a+b). So doing things in that order will lead to this shortcut.

Lets try another order.
Suppose you have rock a, b, c and d.
If you do a-d, then b-c, then (a-d)-(b-c).
Then (a-d)-(b-c) is the same as a-d-b+c, which is the same as -d-b+a+c, which is -(d+b)+(a+c), which is (a+c)-(d+b). Another shortcut.

Then you can see that depending on the order of the subtractions, we get a different setting of difference between two groups.
"""
class Solution:
    def (self, stones: List[int]) -> int:
        half_limit = sum(stones) // 2
        f = [0] * (half_limit + 1) 

        for w in stones:
            for j in range(half_limit,-1,-1):
                if j >= w:
                    f[j] = max(f[j], f[j - w] + w)
        # print(f)  
        return sum(stones) - 2 * f[-1]
"""
1046. Last Stone Weight
Easy, Heap data structure, trick for max heap
Hint: Simulate the process. We can do it with a heap, or by sorting some list of stones every time we take a turn.
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:  
        stones = list(map(lambda item: item * -1, stones))
        from heapq import heappop, heappush, heapify 
        heapify(stones)
        while len(stones) > 1:
            most_heavy_stone = heapq.heappop(stones)
            second_heavy_stone = heapq.heappop(stones)       
            new_stone = most_heavy_stone - second_heavy_stone
            if new_stone < 0:
                heapq.heappush(stones, new_stone)
            # print(stones)
        if len(stones) == 0:
            return 0
        else:
            return heapq.heappop(stones) * (-1)
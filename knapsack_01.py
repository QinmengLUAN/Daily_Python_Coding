"""
Knapsack: 0/1 problem
Solution: DP
Link to explanation: https://coderpad.io/2PR72ZMC/playback#3269
# (the first line contains 2 numbers, 1st is the capacity of the bag, and the 2nd
# number is the total number of items. Then, there are that number lines of input,
# one for each item. Each line contains two numbers, as well. 1st for that item's
# weight, and 2nd for its value. Assume we have 4 items here, and the backpack can
# afford a max total weight of 10. then the input looks like:
#
#   10  4
#   val weight
#   5 4
#   3 2
#   10 8
#   4 8
"""
class Solution:
    # Method 1: table filling
    # f[i][v]=max{ f[i-1][v],f[i-1][v-w[i]]+val[i] }
    def knapsack01(self, info):
        if len(info) <= 1:
            return 0
        weight_limit = info[0][0]
        item_limit = info[0][1]

        f = [[0] * (weight_limit + 1) for i in range(item_limit + 1)]
        for i in range(1, item_limit + 1):
            for w in range(1, weight_limit + 1):
                if w < info[i][0]:
                    f[i][w] = f[i-1][w]
                else:
                    f[i][w] = max(f[i-1][w], f[i-1][w-info[i][0]] + info[i][1])
        print(f)
        return f[-1][-1]

info = [[10, 4], [4, 5], [2, 3], [8, 10], [8, 4]]
s = Solution()
print(s.knapsack01(info))

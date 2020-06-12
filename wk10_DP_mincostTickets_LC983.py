"""
983. Minimum Cost For Tickets
Medium: DP, recursion + cache
Time complexity: O(N*3)
Space complexity: O(N)

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
"""
# Method 1: Recursion + Cache
class Solution:
    def mincostTickets_2(self, days, costs):
        return self.helper(days, costs, 0, {})

    def helper(self, days, costs, i, cache):
        if i >= len(days):
            return 0
        elif i in cache:
            return cache[i]
        else:
            cost_day = costs[0] + self.helper(days, costs, i + 1, cache)
            
            cost_wk = costs[1]
            for j in range(i, len(days)):
                if days[j] - days[i] >= 7:
                    cost_wk = costs[1] + self.helper(days, costs, j, cache)
                    break
            cost_month = costs[2]
            for j in range(i, len(days)):
                if days[j] - days[i] >= 30:            
                    cost_month = costs[2] + self.helper(days, costs, j, cache)
                    break
            res = min(cost_day, cost_wk, cost_month)
            cache[i] = res
        return res

# Method 2: DP_Table filling
class Solution:
    def mincostTickets(self, days, costs):
        table = [0] * 400
        dayset = set(days)
        for i in range(398, -1, -1):
            if i in dayset:
                costs_day = costs[0] + table[i + 1]
                costs_wk = costs[1] + table[i + 7]
                costs_month = costs[2] + table[i +30]
                table[i] = min(costs_day, costs_wk, costs_month)
            else:
                table[i] = table[i + 1]
        print(table)
        return table[0]


days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
s = Solution()
print(s.mincostTickets(days, costs))
 
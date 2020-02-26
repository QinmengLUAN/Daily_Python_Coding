"""
Best time to buy and sell stock

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

"""
class Solution:
	def maxProfit(self, prices):
		min_price = prices[0]
		profit = 0
		for i in range(1,len(prices)):
			if prices[i]< min_price:
				min_price = prices[i]
			current_profit = prices[i] - min_price

			if profit < current_profit:
				profit = current_profit

		return profit



p = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(p))

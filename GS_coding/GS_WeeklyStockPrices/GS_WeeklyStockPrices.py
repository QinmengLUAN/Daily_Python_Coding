"""
https://leetcode.com/discuss/interview-question/487462/Weekly-stock-price-or-OA-2020-or-GS/433198
"""
class Solution:
    def weekAvgStockPrice(self, dailyPrice):
        n = len(dailyPrice)
        if n < 7: return []
        
        out = []
        add = 0
        for i, price in enumerate(dailyPrice):
            add += price
            if i > 5:
                if i > 6: 
                    add -= dailyPrice[i-7]
                out.append(round(add/7, 2))
        return out

s = Solution()
dailyPrice = [5,5,5,5,5,5,5,6,6]
print(s.weekAvgStockPrice(dailyPrice))
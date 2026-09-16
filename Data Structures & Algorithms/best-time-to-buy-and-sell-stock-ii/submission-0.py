class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 0
        sell_price = 0
        profit = 0

        i = 0
        j = 0
        while i < len(prices):
            while (i + 1) < len(prices) and prices[i + 1] < prices[i]:
                i += 1
            buy_price = prices[i]
            j = i
            while (j + 1) < len(prices) and prices[j + 1] > prices[j]:
                j += 1
            sell_price = prices[j]
            profit += sell_price - buy_price
            i = j + 1
        return profit
# Buy: after it goes down, then it'll go up next
# Sell: the day it goes up

#7 1 5 3 6 4
#i j
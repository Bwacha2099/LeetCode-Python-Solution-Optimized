#URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        Find the maximum profit that can be obtained from a series of stock prices.

        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit += price - min_price
                min_price = price

        return max_profit

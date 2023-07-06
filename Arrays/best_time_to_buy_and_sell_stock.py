#URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        Find the maximum profit that can be achieved by buying and selling stocks.

        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

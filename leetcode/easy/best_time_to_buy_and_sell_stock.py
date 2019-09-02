# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value_before = []
        min_value = math.inf

        for val in prices:
            min_value_before.append(min_value)
            if val < min_value:
                min_value = val

        max_profit = 0
        for buy_price, sell_price in zip(min_value_before, prices):
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit

        return max_profit


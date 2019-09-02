# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value_before = []
        max_value_after = []

        min_value = math.inf
        for val in prices:
            min_value_before.append(min_value)
            if val < min_value:
                min_value = val

        max_value = -math.inf
        for val in prices[::-1]:
            max_value_after.append(max_value)
            if val > max_value:
                max_value = val
        max_value_after = max_value_after[::-1]

        second_transaction_profit = [] # profit made if we bought second transaction on day i
        first_transaction_profit = [] # profit made if we sold first transcation on day i

        for val, min_before, max_after in zip(prices, min_value_before, max_value_after):
            first_transaction_profit.append(max(0, val - min_before))
            second_transaction_profit.append(max(0, max_after - val))

        max_profit_before = []
        max_profit_after = []

        max_profit = 0
        for profit in first_transaction_profit:
            if profit > max_profit:
                max_profit = profit
            max_profit_before.append(max_profit)

        max_profit = 0
        for profit in second_transaction_profit[::-1]:
            max_profit_after.append(max_profit)
            if profit > max_profit:
                max_profit = profit
        max_profit_after = max_profit_after[::-1]

        max_total_profit = 0
        for first_profit, second_profit in zip(max_profit_before, max_profit_after):
            if first_profit + second_profit > max_total_profit:
                max_total_profit = first_profit + second_profit

        return max_total_profit

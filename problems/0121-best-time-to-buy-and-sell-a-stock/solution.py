from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Store min
        min_price = 10e6
        # Maximum profit (result)
        max_profit = 0

        for i in range(len(prices)):
            # Store lowest price so far
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                # Only store a new max profit if the profit is realizable (sell is after buy)
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
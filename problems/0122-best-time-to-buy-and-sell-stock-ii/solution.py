from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Set minimum value found and default total_profit
        min_e = 10e5
        tot_profit = 0

        for i in range(len(prices)):
            # if current price is lower than our minimum
            if prices[i] < min_e:
                # set a new minimum price
                min_e = prices[i]
            else:
                # otherwise immediately sell (execute profit)
                tot_profit += prices[i] - min_e
                # and also immediately buy
                min_e = prices[i]

        return tot_profit
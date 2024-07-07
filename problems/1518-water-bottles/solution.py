class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        full = numBottles
        empty = 0
        while full > 0 or empty >= numExchange:
            res += full
            empty += full
            # for next iter
            full = empty // numExchange
            empty = empty % numExchange

        return res

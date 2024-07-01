from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        con = 0
        for n in arr:
            con = con + 1 if n % 2 == 1 else 0
            if con == 3:
                return True
        return False

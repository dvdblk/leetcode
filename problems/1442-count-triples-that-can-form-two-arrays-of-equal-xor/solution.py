from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr) - 1):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    res += j - i
        return res

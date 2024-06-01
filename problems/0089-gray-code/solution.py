from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        for i in range(2, n + 1):
            # we add x to each reversed element in the res array and append to original res
            x = 2 ** (i - 1)
            res = res + [e + x for e in reversed(res)]
        return res

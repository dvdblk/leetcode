from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperature:
                    prev_i = stack.pop()
                    res[prev_i] = i - prev_i

                stack.append(i)

        return res

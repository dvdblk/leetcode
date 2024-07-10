from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps_back = 0
        for log in logs:
            if log == "../":
                steps_back = max(0, steps_back - 1)
            elif log == "./":
                continue
            else:
                steps_back += 1
        return steps_back

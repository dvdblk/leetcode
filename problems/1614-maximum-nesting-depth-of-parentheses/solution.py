class Solution:
    def maxDepth(self, s: str) -> int:
        count, max_depth = 0, 0
        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
            max_depth = max(max_depth, count)

        return max_depth

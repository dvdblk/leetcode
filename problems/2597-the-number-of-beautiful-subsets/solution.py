from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """Bitwise O(n*2^n) TLE"""
        n_beautiful = 0

        for i in range(2 ** len(nums)):
            elems = [0] * 2048
            is_beautiful = True
            for j in range(len(nums)):
                e = nums[j]
                if i & (1 << j):
                    if (e - k > 0 and elems[e - k]) or (elems[e + k]):
                        is_beautiful = False
                        break
                    elems[e] = 1

            n_beautiful += is_beautiful

        # don't count empty set
        return n_beautiful - 1

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """DFS but O(2**n)"""

        def dfs(i, seen):
            if i >= len(nums):
                return 0

            if nums[i] in seen:
                return dfs(i + 1, seen)
            else:
                unseen = seen.copy()
                seen[nums[i] - k] = 1
                seen[nums[i] + k] = 1
                return 1 + dfs(i + 1, seen) + dfs(i + 1, unseen)

        return dfs(0, dict())

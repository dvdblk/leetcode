from collections import defaultdict
from typing import List
from math import sqrt


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # edge cases
        if not nums:
            # nums is empty
            return True
        elif len(nums) > 1 and any(n == 1 for n in nums):
            # nums contains '1'
            return False

        # create a graph of all factors
        g = defaultdict(set)
        for n in nums:
            factors = []
            for i in range(2, int(sqrt(n) + 1)):
                if n % i == 0:
                    factors.append(i)
                    factors.append(n // i)

            for factor in factors:
                g[factor].add(n)
                g[n].add(factor)

        # DFS over all factors
        visited = set()
        stack = [nums[0]]

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)

                for edge in g[node]:
                    stack.append(edge)

        # check if all nodes from nums were visited
        return all(n in visited for n in nums)

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """Two pointers"""
        g = sorted(g)
        s = sorted(s)

        n_content_children = 0
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                n_content_children += 1
                i += 1

            j += 1

        return n_content_children

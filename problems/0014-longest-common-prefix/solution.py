from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Worst case O(n^2)"""
        prefix = ""
        while len(prefix) < len(strs[0]):
            new_prefix = strs[0][:len(prefix)+1]
            for i in range(len(strs)):
                if not strs[i].startswith(new_prefix):
                    return prefix
            prefix = new_prefix

        return prefix
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """count 0s and 1s per section, add min(section_0, section_1) to substring count when section changes"""
        n_substrings = prev_count = 0
        cur_count = 1
        prev = s[0]

        for i in range(1, len(s)):
            if s[i] == prev:
                cur_count += 1
            else:
                n_substrings += min(cur_count, prev_count)
                prev_count = cur_count
                cur_count = 1
                prev = s[i]

        return n_substrings + min(cur_count, prev_count)
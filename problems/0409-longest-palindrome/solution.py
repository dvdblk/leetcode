from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter()

        for ch in s:
            counts[ch] += 1

        # resulting length of the palindrome
        length = 0
        # flag whether the char counts contain at least one odd value
        has_odd = False

        # get the even counts
        for k, v in counts.items():
            if v % 2 == 1 and len(counts) > 1:
                # odd case, subtract 1
                v -= 1
                has_odd = True
            length += v

        # increase length if we have at least one odd letter
        if has_odd:
            length += 1

        return length

    def longestPalindrome2(self, s: str) -> int:
        """Faster solution using Counter."""
        c = Counter(s)
        result = 0
        max_odd = 0

        for v in c.values():
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                max_odd = max(max_odd, v)

        return result + 1 if max_odd > 0 else result

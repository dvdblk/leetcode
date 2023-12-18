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
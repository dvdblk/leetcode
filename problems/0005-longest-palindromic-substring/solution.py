class Solution:
    def longestPalindrome(self, s: str) -> str:
        """O(n^2) by checking palindrome at every ch in s efficiently with two pointers"""

        def check_palindrome_at_indices(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1 : r]

        longest = ""

        for i in range(len(s)):
            s_odd = check_palindrome_at_indices(i, i)
            if len(longest) < len(s_odd):
                longest = s_odd

            s_even = check_palindrome_at_indices(i, i + 1)
            if len(longest) < len(s_even):
                longest = s_even

        return longest

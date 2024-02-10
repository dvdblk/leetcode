class Solution:
    def countSubstrings(self, s: str) -> int:
        is_palindrome = lambda x: x == x[::-1]
        n_palindromes = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                n_palindromes += is_palindrome(s[i:j])

        return n_palindromes

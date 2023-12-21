class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """String concatenation"""
        for i in range(1, len(s) // 2 + 1):
            if s[i:] + s[:i] == s:
                return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        """brute force"""
        for i in range(1, len(s) // 2 + 1):
            if s[:i] * (len(s) // i) == s:
                return True

        return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Using a dictionary to count the nr of occurrences of each letter in both strings."""
        if len(s) != len(t):
            return False

        letters = {}

        for i in range(len(s)):
            if letters.get(s[i]) is None:
                letters[s[i]] = 0
            letters[s[i]] += 1

            if letters.get(t[i]) is None:
                letters[t[i]] = 0
            letters[t[i]] -= 1

        for _, val in letters.items():
            if val != 0:
                return False

        return True

    def isAnagram_2(self, s: str, t: str) -> bool:
        """Using sort"""
        return sorted(s) == sorted(t)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Naive"""
        # s to lower alphanum
        s = s.lower()
        s = "".join(filter(str.isalnum, s))

        # check equality of first half of the word with reversed second
        if len(s) % 2 == 0:
            return s[:len(s)//2] == "".join(reversed(s[len(s)//2:]))
        else:
            return s[:len(s)//2] == "".join(reversed(s[1+len(s)//2:]))

    def isPalindrome(self, s: str) -> bool:
        """Time O(2n) -> O(n), Space O(1)"""
        s_clean = []

        for c in s:
            if c.isalnum():
                s_clean.append(c.lower())

        return s_clean == s_clean[::-1]

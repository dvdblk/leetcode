class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

    def toLowerCase(self, s: str) -> str:
        """iterate over ASCII values"""
        res = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                res += chr(ord(ch) + 32)
            else:
                res += ch

        return res
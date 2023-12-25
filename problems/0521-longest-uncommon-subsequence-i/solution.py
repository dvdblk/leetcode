class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # return the longer string if they are not equal
        return -1 if a == b else len(a) if len(a) > len(b) else len(b)

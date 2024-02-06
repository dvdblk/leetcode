class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        gcd = 0
        for i in range(1, len(str2)+1):
            substr = str2[:i]
            l = len(str1) // len(substr)
            if substr * l == str1 and substr * (len(str2) // len(substr)) == str2:
                gcd = i

        return str2[:gcd]

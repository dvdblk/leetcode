class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """O(n^2) time"""
        t = list(t)
        for ch in s:
            t.remove(ch)

        return t[0]


    def findTheDifference2(self, s: str, t: str) -> str:
        """Use a counter dictionary to find the char that is negative

        O(n) time
        """
        c = Counter()

        for i in range(len(s)):
            c[s[i]] += 1
            c[t[i]] -= 1

        # Add the remaining char to counter
        c[t[-1]] -= 1

        return [k for k, v in c.items() if v < 0].pop()

    def findTheDifference3(self, s: str, t: str) -> str:
        """Use XOR to find the difference between chars

        O(n) time
        """

        r = 0
        for ch in s + t:
            r ^= ord(ch)

        return chr(r)
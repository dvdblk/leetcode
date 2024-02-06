class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:
        """Reverse string and reverse words"""
        # this technically makes the solution O(n) space because
        # python doesn't have mutable strings so we have to create a list first which is O(n)
        s = list(s.strip())

        # reverse the entire string
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]

        # remove unnecessary whitespace
        i = 0
        while i < len(s)-1:
            if s[i] == " " and s[i+1] == " ":
                print(i, s.pop(i))
            else:
                i += 1

        # reverse each word
        start = 0
        # append a space to flip the last word as well
        s.append(" ")
        for i in range(len(s)):
            if s[i] == " ":
                s[start:i] = s[start:i][::-1]
                start = i+1
        # remove last space
        s = s[:-1]
        return "".join(s)


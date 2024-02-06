class Solution:
    def reverseVowels(self, s: str) -> str:
        # can also include uppercase here...
        vowels = {"a", "e", "i", "o", "u"}

        s = list(s)

        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                # swap
                s[l], s[r] = s[r], s[l]
            elif s[l].lower() in vowels:
                # move r closer
                r -= 1
                continue
            elif s[r].lower() in vowels:
                # move l closer
                l += 1
                continue

            # move both closer
            l += 1
            r -= 1
        return "".join(s)

    def reverseVowels2(self, s: str) -> str:
        """Stack + two iterations"""
        vowels = set(["a", "e", "i", "o", "u"])
        stack = []

        # add all vowels to stack
        for ch in s:
            if ch.lower() in vowels:
                stack.append(ch)

        # pop all vowels from stack when a vowel is encountered in the og string
        result = ""
        for ch in s:
            if ch.lower() in vowels:
                result += stack.pop()
            else:
                result += ch

        return result
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

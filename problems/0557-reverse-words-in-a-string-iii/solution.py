class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda x: x[::-1], s.split()))

    def reverseWords2(self, s: str) -> str:
        """Two pointers"""
        # Index for position in the sentence and position in a word
        i = start = 0
        res = list(s)
        while i < len(s):
            if s[i] == " " or i == len(s) - 1:
                end = i
                # case for string ending with a letter
                if i == len(s) - 1:
                    # increment end by one to include the last letter in reversal
                    end += 1
                # reverse
                while start < end:
                    res[start], res[end - 1] = res[end - 1], res[start]
                    start += 1
                    end -= 1

                start = i + 1
            i += 1

        return "".join(res)

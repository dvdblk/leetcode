class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        word = ""

        for ch in s:
            if ch in "1234567890":
                n = n * 10 + int(ch)
            elif ch == "[":
                stack.append((n, word))
                word = ""
                n = 0
            elif ch == "]":
                prev_n, prev_word = stack.pop()
                word = prev_word + prev_n * word
            else:
                word += ch

        return word

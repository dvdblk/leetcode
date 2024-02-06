class Solution:
    def compress(self, chars: List[str]) -> int:
        """'Two' pointers"""
        # input chars list pointer for insitu changes
        ptr = 0
        # current amount of same characters in a row
        n_chars = 1
        # append "end of sentence" token to also add the last character count
        chars.append("<EOS>")

        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                n_chars += 1
            else:
                if n_chars == 1:
                    chars[ptr] = chars[i - 1]
                    ptr += 1
                elif n_chars > 9:
                    chars[ptr] = chars[i - 1]
                    n_chars_str = list(str(n_chars))
                    chars[ptr + 1 : ptr + 1 + len(n_chars_str)] = n_chars_str
                    ptr += 1 + len(n_chars_str)
                else:
                    chars[ptr] = chars[i - 1]
                    chars[ptr + 1] = str(n_chars)
                    ptr += 2

                n_chars = 1

        return len(chars[:ptr])

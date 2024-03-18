from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        l = 0

        for word in words:
            chars_left = chars.copy()
            add_to_length = True

            for ch in word:
                if ch in chars_left:
                    chars_left[ch] -= 1
                    if chars_left[ch] == 0:
                        del chars_left[ch]
                else:
                    add_to_length = False
                    break

            if add_to_length:
                l += len(word)

        return l

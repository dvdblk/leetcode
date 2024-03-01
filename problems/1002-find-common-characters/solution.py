from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])

        for i in range(1, len(words)):
            word = words[i]
            c &= Counter(word)

        res = []
        for letter, count in c.items():
            for _ in range(count):
                res.append(letter)

        return res

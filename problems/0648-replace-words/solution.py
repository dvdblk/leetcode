from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        dictionary.sort(key=len)

        for i, word in enumerate(words):
            for d in dictionary:
                if word[: len(d)] == d:
                    words[i] = d
                    break

        return " ".join(words)

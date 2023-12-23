from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """Set difference of rows and words"""
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        one_row_words = []
        for word in words:
            n_rows = 0
            for row in [first_row, second_row, third_row]:
                # check how many rows does the lowered word match
                if set(word.lower()).difference(row) == set():
                    n_rows += 1

                if n_rows > 1:
                    break

            if n_rows == 1:
                one_row_words.append(word)

        return one_row_words

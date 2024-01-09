class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = Counter(filter(lambda ch: ch.isalpha(), licensePlate.lower()))
        shortest_word = "x" * 1001

        for word in words:
            tmp_letters = letters.copy()
            for ch in word:
                if tmp_letters[ch] > 0:
                    tmp_letters[ch] -= 1

            if all([letter == 0 for letter in tmp_letters.values()]):
                if len(shortest_word) > len(word):
                    shortest_word = word

        return shortest_word

    def shortestCompletingWord2(self, licensePlate: str, words: List[str]) -> str:
        """Using Counter difference"""
        letters = Counter(filter(lambda ch: ch.isalpha(), licensePlate.lower()))
        return min([word for word in words if not(letters - Counter(word))], key=len)

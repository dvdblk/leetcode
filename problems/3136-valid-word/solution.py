class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()

        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        vowels = set(["a", "e", "i", "o", "u"])
        letters = [chr(ord("a") + i) for i in range(27)]
        consonants = list(set(letters) - set(vowels))
        valid_chars = set([str(i) for i in range(10)] + letters)
        for ch in word:
            if ch not in valid_chars:
                return False

            if ch in vowels:
                has_vowel = True

            if ch in consonants:
                has_consonant = True

        return has_vowel and has_consonant

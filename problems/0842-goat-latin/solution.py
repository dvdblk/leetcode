class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        for i, word in enumerate(words):
            if word[0].lower() in ["a", "e", "i", "o", "u"]:
                words[i] = word + "ma"
            else:
                words[i] = word[1:] + word[0] + "ma"

            words[i] += "a" * (i + 1)

        return " ".join(words)
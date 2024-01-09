class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # filter non alpha chars and split into words
        paragraph_filtered = ""
        for char in paragraph:
            if char == " ":
                paragraph_filtered += char
            elif char.isalpha():
                paragraph_filtered += char.lower()
            else:
                paragraph_filtered += " "
        words = paragraph_filtered.split()

        # count words and discard banned
        words_counter = Counter(words)
        for banned_word in banned:
            words_counter[banned_word] = 0

        # return most common one
        return words_counter.most_common(1)[0][0]
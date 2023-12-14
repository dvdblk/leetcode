class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # check for bijection aka use two dicts
        word_to_pat = {}
        pat_to_word = {}

        words = s.split()

        if len(words) != len(pattern):
            return False

        for word, pat in zip(words, pattern):
            if previous_word := pat_to_word.get(pat):

                # if word already present
                if previous_word != word:
                    return False
            else:
                pat_to_word[pat] = word

                # if pattern already present
                if previous_pat := word_to_pat.get(word):
                    if previous_pat != pat:
                        return False
                else:
                    word_to_pat[word] = pat

        return True

    def wordPattern_2(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        # Check for bijection by using zip
        return len(set(words)) == len(set(pattern)) == len(set(zip(words, pattern)))


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon_words = set()
        s1_words = set()
        for word in s1.split():
            if word not in uncommon_words:
                if word not in s1_words:
                    uncommon_words.add(word)
            else:
                uncommon_words.remove(word)
            s1_words.add(word)

        s2_words = set()
        for word in s2.split():
            if word in uncommon_words:
                uncommon_words.remove(word)
            else:
                if word not in s1_words and word not in s2_words:
                    uncommon_words.add(word)

            s2_words.add(word)

        return list(uncommon_words)

    def uncommonFromSentences2(self, s1: str, s2: str) -> List[str]:
        return [k for k, v in Counter(s1.split() + s2.split()).items() if v == 1]
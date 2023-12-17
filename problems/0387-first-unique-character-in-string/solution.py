class Solution:
    def firstUniqChar(self, s: str) -> int:
        # dict of tuple (char, index) to keep track of duplicit elems
        chars = dict()

        indices = []
        for i in range(len(s)):
            if s[i] in chars.keys():
                # element already inside, this char is duplicit
                # remove it from indices
                if s[i] in indices:
                    indices.remove(s[i])
            else:
                indices.append(s[i])
                chars[s[i]] = i

        return chars.get(indices[0]) if indices else -1

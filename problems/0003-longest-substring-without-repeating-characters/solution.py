class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = 0
        longest = 0
        characters = dict()

        for i, ch in enumerate(s):
            prev_index = characters.get(ch)
            if prev_index is not None:
                cur = i - prev_index
                new_characters = dict()
                for prev_ch, prev_i in characters.items():
                    if prev_i >= prev_index:
                        new_characters[prev_ch] = prev_i
                characters = new_characters
            else:
                cur += 1

            characters[ch] = i
            longest = max(longest, cur)

        return longest
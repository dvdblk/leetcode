class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """O(n)"""
        # Result
        len_after_space = 0
        # Flag to reset the counting
        reset = False
        for i in range(len(s)):
            if s[i] == " ":
                # set reset flag
                reset = True
            else:
                # if reset flag is set
                if reset:
                    # start counting from 0 again because we encountered another letter after n spaces
                    len_after_space = 0
                    reset = False
                # bump the length
                len_after_space += 1

        return len_after_space

    def lengthOfLastWord_faster(self, s: str) -> int:
        """O(n) but begin at the end of the list"""

        len_of_last_word = 0
        # iterate backwards
        for i in range(len(s) - 1, -1, -1):
            # if whitespace
            if s[i] == " ":
                # check if there is some existing length
                if len_of_last_word == 0:
                    # if not, then continue looking for at least 1 character
                    continue
                else:
                    # if there is, return the result
                    break
            else:
                # add length if we find characters
                len_of_last_word += 1

        return len_of_last_word

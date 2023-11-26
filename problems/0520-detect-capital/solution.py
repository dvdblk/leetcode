class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # Initial values for each case
        case1 = word[0].isupper()
        case2 = word[0].islower()
        case3 = word[0].isupper()

        # Keep track of each case separately
        for i in range(1, len(word)):
            if case1:
                case1 = word[i].isupper()

            if case2:
                case2 = word[i].islower()

            if case3:
                case3 = word[i].islower()

        # Return one of them
        return case1 or case2 or case3
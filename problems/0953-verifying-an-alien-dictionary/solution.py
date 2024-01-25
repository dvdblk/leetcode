class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {order[i]: i for i in range(len(order))}

        for i_w in range(len(words)-1):
            l = min(len(words[i_w]), len(words[i_w+1]))
            for i in range(l):
                # get letters in one column
                a, b = alphabet[words[i_w][i]], alphabet[words[i_w+1][i]]
                if a > b:
                    # first letter is lexicographically higher, return False
                    return False
                elif a < b:
                    # if first letter is strictly lexicographically lower, we don't need to continue
                    break

            # check if the first word isn't longer than the second if the second is prefix of first
            if l == len(words[i_w+1]) and words[i_w] != words[i_w+1] and words[i_w][:l] == words[i_w+1]:
                return False
        return True
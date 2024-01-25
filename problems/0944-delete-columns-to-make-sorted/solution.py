class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = [0 for _ in range(len(strs[0]))]
        result = 0
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if cols[j] is None:
                    continue

                if cols[j] > ord(strs[i][j]):
                    result += 1
                    cols[j] = None
                else:
                    cols[j] = ord(strs[i][j])

        return result

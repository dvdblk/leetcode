class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """O(n)"""
        prev_c_idx = None
        occurences = []

        for i, char in enumerate(s):
            if char == c:
                if prev_c_idx is None:
                    # replace None vals with distance to first c
                    for j in range(i):
                        occurences[j] = i - j
                else:
                    # replace None vals with shortest distance to any c
                    for j in range(prev_c_idx, i):
                        occurences[j] = min(i-j, j-prev_c_idx)
                occurences.append(0)
                prev_c_idx = i
            else:
                # add None val if s[i] is not c
                occurences.append(None)

            # replace leftover None vals if end reached
            if i == len(s) - 1:
                for j in range(prev_c_idx, i+1):
                    occurences[j] = j - prev_c_idx


        return occurences
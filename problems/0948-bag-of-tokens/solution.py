from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        score = 0
        tokens.sort()
        left = 0
        right = len(tokens) - 1

        while left <= right:
            # Greedy, always decrease power if possible
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score

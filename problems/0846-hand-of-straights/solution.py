from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        c = Counter(hand)

        for card in hand:
            if c[card]:
                for following_card in range(card, card + groupSize):
                    if c[following_card] == 0:
                        return False
                    c[following_card] -= 1

        return True

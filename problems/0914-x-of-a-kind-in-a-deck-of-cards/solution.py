class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        elif len(deck) == 2:
            return True

        c = Counter(deck)
        for n in range(2, len(deck)):
            divisible = True
            for val in c.values():
                if val % n != 0:
                    divisible = False

            if divisible:
                return True

        return False
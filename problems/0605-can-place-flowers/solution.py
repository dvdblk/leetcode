class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """'Sliding window'"""
        # pad with 0s
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            # stop early if no more flowers to place
            if n == 0:
                return True

            # check for [..., 0, 0, 0, ...]
            if flowerbed[i-1:i+2] == [0, 0, 0]:
                n -= 1
                flowerbed[i] = 1

        return n == 0
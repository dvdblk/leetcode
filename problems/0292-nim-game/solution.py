class Solution:
    def canWinNim(self, n: int) -> bool:
        # if the number if divisible by 4, then we always lose
        if n % 4 == 0:
            return False

        # otherwise we can always win
        return True
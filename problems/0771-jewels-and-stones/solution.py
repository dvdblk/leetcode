class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        stones = Counter(stones)
        n_jewels = 0
        for jewel in jewels:
            n_jewels += stones[jewel]
        return n_jewels
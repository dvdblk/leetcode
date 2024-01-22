class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """Brute force - TLE"""
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        for a in aliceSizes:
            for b in bobSizes:
                if alice_sum + b - a == bob_sum + a - b:
                    return [a, b]

    def fairCandySwap2(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """linear search math solution"""
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        alice_set = set(aliceSizes)

        delta = (alice_sum - bob_sum) // 2
        for size in bobSizes:
            if delta + size in alice_set:
                return [delta + size, size]

        return [0, 0]
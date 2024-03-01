class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")
        zeros_count = len(s) - ones_count

        return (ones_count - 1) * "1" + zeros_count * "0" + "1"

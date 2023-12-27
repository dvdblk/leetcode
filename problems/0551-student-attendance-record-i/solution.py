class Solution:
    def checkRecord(self, s: str) -> bool:
        """Naive O(n)"""
        n_absent = 0
        n_consecutive_late = 0

        for char in s:
            if char == "L":
                n_consecutive_late += 1
            elif char == "A":
                n_absent += 1
                n_consecutive_late = 0
            elif char == "P":
                n_consecutive_late = 0

            if n_consecutive_late >= 3:
                return False

        return n_absent < 2

    def checkRecord2(self, s: str) -> bool:
        return s.count("A") < 2 and not "LLL" in s

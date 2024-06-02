class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_nr = 0

        for i in range(len(number)):
            if number[i] == digit:
                max_nr = max(max_nr, int(number[:i] + number[i + 1 :]))

        return str(max_nr)

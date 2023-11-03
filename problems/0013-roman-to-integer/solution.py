from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        """Dict + """
        def convert(subs: str) -> int:
            vals = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900,
                "III": 3,
                "II": 2
            }
            return vals.get(subs)

        res = 0
        r = 0
        while len(s) > 0:
            val = convert(s[:r+1])
            if val is not None:
                r += 1
                if r == len(s):
                    return res+val
            else:
                res += convert(s[:r])
                s = s[r:]
                r = 0

        return res

    def romanToInt(self, s: str) -> int:
        res = 0
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # This solution leverages the fact that the roman number format is
        # mostly in a descending order
        for i in range(len(s)-1):
            cur_number = roman_to_int[s[i]]
            next_number = roman_to_int[s[i+1]]
            # If the next number is larger
            if cur_number < next_number:
                # Subtract current number
                res -= cur_number
            else:
                # Otherwise if next is smaller, add the current one
                res += cur_number

        # Don't forget about the last number which is always added
        last_number = roman_to_int[s[-1]]
        return res + last_number

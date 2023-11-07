from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Add one from the back
        digits[-1] = digits[-1] + 1

        # flag to optionally add a new digit
        fix_first_digit = False
        # Update the rest of the number if needed
        # in reverse
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9:
                # only keep the ones part of each list element
                digits[i] = digits[i] % 10
                if i - 1 >= 0:
                    # add one to the next number
                    digits[i - 1] = digits[i - 1] + 1
                else:
                    fix_first_digit = True
            else:
                # we can stop early if digits[i] <= 9
                break

        if fix_first_digit:
            digits.insert(0, 1)

        return digits

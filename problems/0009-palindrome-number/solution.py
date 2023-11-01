class Solution:
    def isPalindrome_1(self, x: int) -> bool:
        """Naive solution with two loops and two pointers

        Time O(2n) = O(n)
        """
        if x < 0:
            return False

        digits = []
        n = 0
        while x > 0:
            last_dig = x % 10
            digits.insert(0, last_dig)
            x = x // 10
            n += 1

        if n == 1:
            return True
        elif n == 2:
            return digits[0] == digits[1]

        l = r = 0
        for i in range(n//2):
            if digits[i] != digits[n-1-i]:
                return False
        return True

    def isPalindrom_2(self, x: int) -> bool:
        """
        Time O(n), Space O(1)
        """
        if x < 0:
            return False
        elif x < 10:
            return True

        # Construct a number from the last digits recursively
        x_mirror = 0
        while x > x_mirror:
            # get new digit
            new_digit = x % 10
            if new_digit == 0 and x_mirror == 0:
                # edge case for when the number is ending with 0
                return False
            # multiply previous mirrored x by 10
            x_mirror *= 10
            # add new digit
            x_mirror += new_digit

            # remove digit from x
            x = x // 10

        # need to account for two cases
        # 1. even number of digits => comparison of x and x_mirror
        even_case = x == x_mirror
        # 2. odd => remove the last digit from x_mirror and compare
        odd_case = x == x_mirror // 10 and x_mirror // 10 != 0
        return even_case or odd_case
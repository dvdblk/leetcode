class Solution:
    def isHappy(self, n: int) -> bool:
        happy = False
        # Keep a set of visited/used numbers
        used = set()

        while not happy:
            # Get sum of digits
            sum_of_digits = 0
            while n > 0:
                sum_of_digits += (n % 10) ** 2
                n = n // 10

            if sum_of_digits in used:
                # Stuck in a loop
                happy = False
                break
            elif sum_of_digits == 1:
                # Found the happy number
                happy = True
                break
            else:
                # Update n to the sum
                n = sum_of_digits
                # Visited sum_of_digits
                used.add(sum_of_digits)

        return happy

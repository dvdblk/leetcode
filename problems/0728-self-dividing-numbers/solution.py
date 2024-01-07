class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # resulting list of all self dividing numbers
        numbers = []

        for i in range(left, right+1):
            num = i
            is_self_dividing = True

            # iterate over all digits and check if they divide i
            while num > 0:
                digit = num % 10
                num //= 10
                if not digit or i % digit != 0:
                    is_self_dividing = False
                    break

            # append i to the result
            if is_self_dividing:
                numbers.append(i)

        return numbers
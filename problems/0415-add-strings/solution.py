class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Reverse strings to start with
        num1 = num1[::-1]
        num2 = num2[::-1]

        # pad shorter with with 0s
        if len(num1) != len(num2):
            if len(num1) > len(num2):
                num2 += "0" * (len(num1) - len(num2))
            else:
                num1 += "0" * (len(num2) - len(num1))

        result = ""
        carry = 0
        for i in range(len(num1)):
            total = int(num1[i]) + int(num2[i]) + carry
            carry = total // 10
            new = total % 10
            result += str(new)

        # handle last carry
        if carry:
            result += str(carry)

        return result[::-1]



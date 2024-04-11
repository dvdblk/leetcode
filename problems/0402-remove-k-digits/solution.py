class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return ""

        stack = [num[0]]

        for i in range(1, len(num)):

            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1

            stack.append(num[i])

        while k > 0:
            stack.pop()
            k -= 1

        res = "".join(stack).lstrip("0")
        return "0" if res == "" else res

class Solution:
    def checkValidString(self, s: str) -> bool:
        """O(n) two passes"""
        # stack for asterisks
        asterisks = []
        # for opening brackets '(' that are not closed yet
        stack = []

        for i, ch in enumerate(s):
            if ch == ")":
                if stack:
                    stack.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
            elif ch == "(":
                stack.append(i)
            elif ch == "*":
                asterisks.append(i)

        # clean up the stack of open brackets with asterisks
        while stack:
            last = stack.pop()
            if not asterisks:
                return False

            # only valid stack removal if last asterisk is after the open bracket
            last_asterisk = asterisks.pop()
            if last_asterisk <= last:
                return False

        return not stack

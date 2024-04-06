class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # indices we know will for sure be removed
        to_remove = [0 for _ in s]
        # stack for open parentheses that need to be closed (removed)
        stack = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove[i] = 1

        # add elements from stack to indices that need to be removed
        for i in stack:
            to_remove[i] = 1

        # build result
        res = ""
        for i, ch in enumerate(s):
            if not to_remove[i]:
                res += ch

        return res

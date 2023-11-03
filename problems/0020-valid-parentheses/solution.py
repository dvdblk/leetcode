class Solution:

    def isValid(self, s: str) -> bool:
        """Naive stack approach"""
        brackets_left = ""
        for i in range(len(s)):

            match s[i]:
                case "(":
                    brackets_left = ")" + brackets_left
                case "{":
                    brackets_left = "}" + brackets_left
                case "[":
                    brackets_left = "]" + brackets_left
                case "]" | "}" | ")":
                    if brackets_left == "" or brackets_left[0] != s[i]:
                        return False
                    else:
                        brackets_left = brackets_left[1:]

        return brackets_left == ""

    def isValid_stack(self, s: str) -> bool:

        stack = []
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for bracket in s:
            if bracket in brackets:
                # Add a new opening bracket to the stack
                stack.append(bracket)
            else:
                # return False if the stack is empty and current bracket is a closing one
                if len(stack) == 0:
                    return False

                # if the type of the bracket is different than expected return False
                last_closing_bracket = brackets[stack.pop()]
                if bracket != last_closing_bracket:
                    return False

        return len(stack) == 0
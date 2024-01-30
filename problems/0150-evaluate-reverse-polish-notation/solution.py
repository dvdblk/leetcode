class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        result = None
        while tokens:
            token = tokens.pop(0)
            if token.lstrip("-").isdigit():
                operand_stack.append(int(token))
            else:
                op_2, op_1 = operand_stack.pop(), operand_stack.pop()

                if token == "+":
                    result = op_1 + op_2
                elif  token == "-":
                    result = op_1 - op_2
                elif token == "*":
                    result = op_1 * op_2
                elif token == "/":
                    result = int(op_1 / op_2)

                operand_stack.append(result)

        return operand_stack.pop()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '/', '*']
        stack = []

        for token in tokens:
            if token in ops:


                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(token)

        return int(stack.pop())

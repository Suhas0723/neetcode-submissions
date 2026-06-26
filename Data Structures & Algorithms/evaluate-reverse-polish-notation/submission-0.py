class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", '-', '*', '/']
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                elif i == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b/a))
        
        return stack[0]


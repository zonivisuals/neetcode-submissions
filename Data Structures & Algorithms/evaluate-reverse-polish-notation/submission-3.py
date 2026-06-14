class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            print(stack)
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                v1 = stack.pop()
                stack.append(stack.pop() - v1)
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                v1 = stack.pop()
                stack.append(int(stack.pop() / v1))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
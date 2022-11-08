class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        for item in tokens:
            if item not in operands:
                stack.append(int(item))
                continue
            elif item == "+":
                res = stack[-2] + stack[-1]
            elif item == "-":
                res = stack[-2] - stack[-1]
            elif item == "*":
                res = stack[-2] * stack[-1]
            elif item == "/":
                res = int(stack[-2] / stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res)
            
        return stack[0]
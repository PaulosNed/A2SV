class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for p in s:
            if p == "(":
                stack.append(0)
            else:
                popped = stack.pop()
                if popped == 0:
                    if stack:
                        stack[-1] += 1
                    else:
                        ans += 1
                else:
                    popped *= 2
                    if stack:
                        stack[-1] += popped
                    else:
                        ans += popped
        return ans
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        tracker = {}
        stack = []
        for j, v in enumerate(s):
            tracker[v] = j

        for i, l in enumerate(s):
            if l not in stack:
                while (stack and stack[-1] > l and tracker[stack[-1]] > i):
                    stack.pop()

                stack.append(l)

        return ''.join(stack)
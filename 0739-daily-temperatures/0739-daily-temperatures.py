class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                idx, val = stack.pop()
                ans[idx] = i -idx
            stack.append([i, v])
        return ans
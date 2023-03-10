class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)
        optimized = float("inf")
        def backtrack(cIdx, kids):
            nonlocal optimized
            
            if cIdx >= len(cookies):
                optimized = min(optimized, max(kids))
                return
                
            for i in range(len(kids)):
                temp = kids[:]
                temp[i] += cookies[cIdx]
                backtrack(cIdx + 1, temp)
                
        backtrack(0, [0] * k)
        return optimized
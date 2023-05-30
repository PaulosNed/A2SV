class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        def dp(n, memo):
            if n <= 1:
                return n

            if n not in memo:
                memo[n] = dp(n//2, memo)
                if n%2 != 0:
                    memo[n] += dp((n//2) + 1, memo)

            return memo[n]
        
        memo = defaultdict(int)
        for i in range(n, -1, -1):
            dp(i, memo)
        
        return max(memo.values())
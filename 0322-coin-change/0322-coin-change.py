class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(curr, memo):
            if curr == 0:
                return 0
            
            if curr < 0:
                return float("inf")
            
            if curr not in memo:
                for coin in coins:
                    memo[curr] = min(memo[curr], dp(curr-coin, memo) + 1)
            
            return memo[curr]
                    
        memo = defaultdict(lambda: float('inf'))
        ans = dp(amount, memo)
        return ans if ans != float("inf") else -1 
        
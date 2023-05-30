class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        def dp(i, memo):
            if i >= len(cost):
                return 0
            
            if i not in memo:
                opt1 = dp(i+1, memo)
                opt2 = dp(i+2, memo)
                memo[i] += min(opt1, opt2) + cost[i]
                
            return memo[i]
        
        memo = defaultdict(int)
        
        ans1 = dp(0, memo)
        ans2 = dp(1, memo)
        
        return min(ans1, ans2)
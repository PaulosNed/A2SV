class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(idx, max_days):
            if idx == len(days):
                return 0
            
            if days[idx] < max_days:
                return dp(idx + 1, max_days)
            
            opt1 = costs[0] + dp(idx + 1, days[idx])
            opt2 = costs[1] + dp(idx + 1, days[idx] + 7)
            opt3 = costs[2] + dp(idx + 1, days[idx] + 30)
            
            return min(opt1, opt2, opt3)
        
        return dp(0, 0)
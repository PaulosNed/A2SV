class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        
        @cache
        def dp(idx, cnt1, cnt2):
            if idx >= len(stones):
                return abs(cnt1 - cnt2)
            
            option1 = dp(idx+1, cnt1 + stones[idx], cnt2)
            option2 = dp(idx+1, cnt1, cnt2 + stones[idx])
            
            return min(option1, option2)
        
        return dp(0, 0, 0)
            
            
            
            
            
            
        
        
        
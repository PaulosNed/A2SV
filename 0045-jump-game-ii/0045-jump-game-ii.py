class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @cache
        def dp(idx):
            if idx >= len(nums) - 1:
                return 0
            
            ans = float("inf")
            for i in range(idx + 1, idx + 1 + nums[idx]):
                ans = min(ans, 1 + dp(i))
            
            return ans
        
        return dp(0)
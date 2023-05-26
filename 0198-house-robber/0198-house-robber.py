class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(curr):
            if curr >= len(nums) - 2:
                return max(nums[curr:])
            
            if curr not in memo:
                opt1 = dp(curr + 1)
                opt2 = nums[curr] + dp(curr + 2)
                memo[curr] = max(opt1, opt2)
            
            return memo[curr]
        
        memo = {}
        return dp(0)
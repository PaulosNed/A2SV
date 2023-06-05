class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(curr, idx, memo):
            if idx == len(nums) and curr == target:
                return 1
            
            if idx >= len(nums):
                return 0
            
            state = (curr, idx)
            if state not in memo:
                memo[state] += dp(curr + nums[idx], idx+1, memo)
                memo[state] += dp(curr - nums[idx], idx+1, memo)
            
            return memo[state]
        
        memo = defaultdict(int)
        return dp(0, 0, memo)
        
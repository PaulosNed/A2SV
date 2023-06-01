class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(idx, canRob, memo):
            if idx >= len(nums):
                return 0
            
            if not canRob:
                return dp(idx+1, True, memo)
            
            state = (idx, canRob)
            if state not in memo:
                option1 = nums[idx] + dp(idx+1, False, memo)
                option2 = dp(idx+1, True, memo)
                memo[state] = max(option1, option2)
            
            return memo[state]
        
        initial = nums[:]
        
        nums = nums[:-1]
        option1 = dp(0, True, defaultdict(int))
        
        nums = initial[1:]
        option2 = dp(0, True, defaultdict(int))
        
        return max(option1, option2)
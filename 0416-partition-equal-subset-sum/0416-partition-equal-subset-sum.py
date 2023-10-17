class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        target = total / 2
        
        @cache
        def dp(idx, curr):
            nonlocal target
            
            if curr == target:
                return True
            
            if curr > target:
                return False
            
            if idx >= len(nums):
                return False
            
            opt1 = dp(idx + 1, curr + nums[idx])
            
            if opt1:
                return opt1
            
            else:
                return dp(idx + 1, curr)
            
        
        return dp(0, 0)
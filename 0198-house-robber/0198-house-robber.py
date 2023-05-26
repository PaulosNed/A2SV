class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        def dp(curr, memo):
            if curr <= 1:
                return nums[curr]

            if curr == 2:
                return nums[curr] + nums[0]

            if curr not in memo:
                memo[curr] = nums[curr] + max(dp(curr - 2, memo) , dp(curr - 3, memo))     
            
            return memo[curr]
        
        memo = defaultdict(int)
        max_1 = dp(len(nums) - 1, memo)
        max_2 = dp(len(nums) - 2, memo)
        
        return max(max_1, max_2)
        
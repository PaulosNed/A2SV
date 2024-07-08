class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = [0] * n
        dp[n - 1] = 1
        
        m = 0
        for c in range(k + 1):
            eq = defaultdict(int)
            eq[nums[n - 1]] = dp[n - 1]
            
            for i in range(n - 2, -1, -1):
                ndp = 1 + max(eq[nums[i]], m)
                
                eq[nums[i]] = ndp
                m = max(m, dp[i])
                
                dp[i] = ndp
                
            m = dp[n - 1]
            
        return max(dp)    
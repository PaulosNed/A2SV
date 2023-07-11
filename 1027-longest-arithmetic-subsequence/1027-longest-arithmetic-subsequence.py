class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        ans = 2
        memo = [defaultdict(lambda: 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                memo[i][diff] = memo[j][diff] + 1
                ans = max(ans, memo[i][diff])
        
        return ans
        
                
        
        
            
                
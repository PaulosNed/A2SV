class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        ps = 0
        ans = 0
        
        for i in range(len(nums)):
            ps += nums[i]
            ans = max(ans, ceil(ps / (i+1)))
        
        return ans
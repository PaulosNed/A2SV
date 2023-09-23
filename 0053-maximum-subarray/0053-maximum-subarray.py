class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ps = [0]
        ans = max(nums)
        
        for idx, num in enumerate(nums):
            curr = ps[-1] + num
            ps.append(curr)
        
        min_val = 0
        for i in range(1, len(ps)):
            if ps[i] < min_val:
                min_val = ps[i]
            
            else:
                ans = max(ans, ps[i] - min_val)
        
        return ans
        
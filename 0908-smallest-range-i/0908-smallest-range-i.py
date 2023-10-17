class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        min_val = min(nums)
        max_val = max(nums)
        
        return max(0, max_val - k - (min_val + k))
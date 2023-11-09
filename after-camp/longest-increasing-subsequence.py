class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ans = [1] * len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            max_val = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_val = max(max_val, 1 + ans[j])
            ans[i] = max_val
        
        return max(ans)
                
        
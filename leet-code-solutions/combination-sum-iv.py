class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def backtrack(curr):

            if curr == target:
                return 1
            
            if curr > target:
                return 0
            
            ans = 0
            for i in range(len(nums)):
                curr += nums[i]
                ans += backtrack(curr)
                curr -= nums[i]
            
            return ans
        
        return backtrack(0)
            

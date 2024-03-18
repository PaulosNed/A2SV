class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(start, end):
            if end >= len(nums) - 1:
                # print(nums[end], nums[start])
                return 1 if -target <= nums[end] - nums[start] <= target else -len(nums)
            
            ans = dp(start, end + 1)
            
            if -target <= nums[end] - nums[start] <= target:
                ans = max(ans, 1 + dp(end, end + 1))
            
            return ans
        
        solution = dp(0, 1)
        return solution if solution > 0  else -1
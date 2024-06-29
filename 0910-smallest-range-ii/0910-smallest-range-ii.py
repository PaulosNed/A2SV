class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        N  = len(nums)
        nums.sort()

        score = nums[-1] - nums[0]
        ans = score

        for divider in range(0, N-1):
            maximumAfterDivision = max(nums[divider]    + k , nums[-1] - k)
            minimumAfterDivision = min(nums[divider+1]  - k , nums[0]  + k)
            score = maximumAfterDivision - minimumAfterDivision

            ans = min(ans, score)
        
        return ans
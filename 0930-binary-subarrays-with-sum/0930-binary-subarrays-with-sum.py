class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        ans = 0
        running = 0
        for num in nums:
            running += num
            if running - goal in prefixSum:
                ans += prefixSum[running - goal]
            prefixSum[running] += 1
        return ans
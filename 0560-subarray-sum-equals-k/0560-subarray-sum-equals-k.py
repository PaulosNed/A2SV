class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        running_sum = 0
        ans = 0
        for num in nums:
            running_sum += num
            if running_sum - k in prefixSum:
                ans += prefixSum[running_sum - k]
            prefixSum[running_sum] += 1
        return ans
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        running_sum = 0
        total = 0
        
        for num in nums:
            running_sum += num
            if running_sum%k in prefixSum:
                total += prefixSum[running_sum%k]
            prefixSum[running_sum%k] = prefixSum.get(running_sum%k, 0) + 1
            
        return total
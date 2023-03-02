class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefixSum = [0] * (len(nums) + 1)
        for request in requests:
            prefixSum[request[0]] += 1
            prefixSum[request[1]+1] -= 1
            
        for j in range(len(prefixSum)):
            prefixSum[j] += 0 if j == 0 else prefixSum[j-1]
            
        prefixSum.sort()
        nums.sort()
        prefixSum.reverse()
        nums.reverse()
        i = 0
        ans = 0
        while(i < len(nums)):
            ans += (prefixSum[i] * nums[i])
            i += 1
            
        return ans % (10**9 + 7)
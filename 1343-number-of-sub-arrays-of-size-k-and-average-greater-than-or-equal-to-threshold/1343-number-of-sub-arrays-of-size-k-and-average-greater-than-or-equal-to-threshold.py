from statistics import mean
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        end = k - 1
        currAvg = mean(arr[start:end+1])
        ans = 0
        while(end < len(arr)):
            if currAvg >= threshold:
                ans += 1
            end += 1
            if end < len(arr):
                currAvg = ((currAvg*k) - arr[start] + arr[end]) / k 
            start += 1
        return ans
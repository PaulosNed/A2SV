class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currAvg = sum(nums[0:k]) / k
        avg = currAvg
        end = k
        while(end < len(nums)):
            currAvg -= (nums[end - k] / k)
            currAvg += (nums[end] / k)
            avg = max(avg, currAvg)
            end += 1
        return avg
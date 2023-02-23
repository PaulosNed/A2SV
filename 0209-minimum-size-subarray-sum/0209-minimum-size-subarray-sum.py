class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        minLength = float("inf")
        currSum = 0
        while(end <= len(nums)):
            if currSum >= target:
                minLength = min(minLength, end-start)
                currSum -= nums[start]
                start += 1
            else:
                if end < len(nums):
                    currSum += nums[end]
                end += 1
        if minLength == float("inf"):
            minLength = 0
        return minLength
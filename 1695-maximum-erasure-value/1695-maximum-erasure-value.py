class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        tracker = {}
        ans = 0
        currSum = 0
        while(end < len(nums)):
            if nums[end] in tracker:
                ans = max(ans, currSum)
                idx = tracker.pop(nums[end])
                for i in range(start,idx+1):
                    currSum -= nums[i]
                    if i != idx:
                        tracker.pop(nums[i])
                start = idx + 1
            else:
                tracker[nums[end]] = end
                currSum += nums[end]
                end += 1
        ans = max(ans, currSum)
        return ans
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        found = False
        for i in range(len(nums)):
            if nums[i] == target and found:
                ans[1] = i
            elif nums[i] == target:
                found = True
                ans[0] = i
                ans[1] = i
        return ans
                
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        for idx, num in enumerate(nums):
            if idx > maxIdx:
                return False
            maxIdx = max(maxIdx, idx+num)
        return True
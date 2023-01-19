class Solution(object):
    def sortColors(self, nums):
        if len(nums) < 2:
            return nums
        for _ in range(len(nums)):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums
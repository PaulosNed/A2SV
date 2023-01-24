class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        nonZero = 0
        while(nonZero < len(nums) and zero < len(nums)):
            if nums[zero] == 0 and nums[nonZero] != 0:
                if zero < nonZero:
                    nums[zero], nums[nonZero] = nums[nonZero], nums[zero]
                nonZero += 1
            if zero < len(nums) and nums[zero] != 0:
                zero += 1
            if nonZero < len(nums) and nums[nonZero] == 0:
                nonZero += 1
        
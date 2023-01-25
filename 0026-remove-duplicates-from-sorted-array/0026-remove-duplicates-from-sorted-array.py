class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = 1
        while(i < len(nums)):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        
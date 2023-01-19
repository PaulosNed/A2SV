class Solution(object):
    def sortColors(self, nums):
        i = 0
        while(i<len(nums)):
            minIdx = i
            for j in range(i, len(nums)):
                if nums[j] < nums[minIdx]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
            i += 1
        return nums
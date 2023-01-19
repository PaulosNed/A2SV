class Solution(object):
    def sortColors(self, nums):
        if len(nums) < 2:
            return nums
        i = 1
        while(i<len(nums)):
            if nums[i] < nums[i-1]:
                j = i
                while(nums[j] < nums[j-1]):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j-=1
                    if (j <= 0):
                        break
            i+=1
        return nums
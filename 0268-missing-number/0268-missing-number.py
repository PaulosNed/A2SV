class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(None)
        for i in range(len(nums)):
            while nums[i] != None and nums[i] != i:
                idx = nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]
        
        for i, v in enumerate(nums):
            if v == None:
                return i
               
        return -1
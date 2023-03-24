class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while(nums[i] != i + 1 ):
                idx = nums[i] - 1
                if nums[i] == nums[idx]:
                    break
                nums[i], nums[idx] = nums[idx], nums[i]
        
        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i+1]
        return ans
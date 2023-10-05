class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        rem = 0
        pairs = 0
        
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                pairs += 1
                i += 2
            
            else:
                rem += 1
                i += 1
        
        if i < len(nums):
            rem += 1
            
        return [pairs, rem]
                
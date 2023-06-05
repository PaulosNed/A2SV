class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = [float('inf')] * len(nums)
        prefix = nums[0]
        
        for i in range(len(nums)):
            prefix = min(prefix, nums[i])
            stack[i] = prefix
        
        prefix = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            prefix = max(nums[i], prefix)
            if nums[i] != stack[i] and nums[i] != prefix:
                return True
        
        return False
                
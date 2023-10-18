class Solution:
    def minOperations(self, nums: List[int]) -> int:
        setNums = set(nums)
        length = len(nums)
        erased = length - len(setNums)
        
        nums = list(setNums)
        nums.sort()
        
        start = 0
        end = 0
        max_len = 0
        
        while end < len(nums):
            if start == end:
                end += 1
                continue
            
            if nums[end] <= length + nums[start] - 1:
                end += 1
            
            else:
                max_len = max(max_len, end - start)
                start += 1
        
        max_len = max(max_len, end - start)
        return len(nums) - max_len + erased
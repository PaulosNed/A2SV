class custom:
    def __init__(self, value):
        self.value = value
        
    def __lt__(self, other):
        return str(self.value) + str(other.value) < str(other.value) + str(self.value)
    
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for idx in range(len(nums)):
            nums[idx] = custom(nums[idx])
            
        nums.sort(reverse = True)
        
        for idx in range(len(nums)):
            nums[idx] = str(nums[idx].value)
        
        return str(int("".join(nums)))
        
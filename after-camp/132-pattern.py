class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        middle = float("-inf")
        stack = []
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < middle:
                return True
            while stack and stack[-1] < nums[i]:
                middle = stack.pop()  
            stack.append(nums[i])
            
        return False
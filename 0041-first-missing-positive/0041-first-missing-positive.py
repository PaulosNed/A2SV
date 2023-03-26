class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        postives = set()
        for num in nums:
            if num > 0:
                postives.add(num)
                
        postives = list(postives)        
        postives.sort()
        
        for i, v in enumerate(postives):
            if v != i + 1:
                return i + 1
        
        return postives[-1] + 1 if postives else 1
            
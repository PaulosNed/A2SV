class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        def backtrack(subset, idx):
            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                final.append(subset[:])
                backtrack(subset, i + 1)
                subset.pop()
        
        final.append([])
        backtrack([], 0)
        return final
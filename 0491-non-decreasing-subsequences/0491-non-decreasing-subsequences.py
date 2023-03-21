class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        def backtrack(subset, idx):
            if idx > len(nums):
                return
            
            if len(subset) >= 2:
                final.append(subset[:])
            
            for i in range(idx, len(nums)):
                if subset and nums[i] < subset[-1]:
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        
        backtrack([], 0)
        result = []
        for item in final:
            if item not in result:
                result.append(item)
        return result
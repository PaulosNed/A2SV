class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(curr):
            nonlocal ans
            
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
        
        backtrack([])
        return ans
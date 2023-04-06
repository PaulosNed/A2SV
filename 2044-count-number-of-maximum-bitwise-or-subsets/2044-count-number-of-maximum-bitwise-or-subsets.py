class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for num in nums:
            ans = ans | num
        
        def backtrack(idx, curr):
            nonlocal count
            nonlocal ans
            
            if idx >= len(nums):
                if curr == ans:
                    count += 1
                return
            
            if curr == ans:
                count += 1
            
            for i in range(idx, len(nums)):
                backtrack(i+1, (curr | nums[i]))
                
        backtrack(0, 0)
        return count